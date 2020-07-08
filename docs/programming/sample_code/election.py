# coding=utf-8
# 4 samples for python async
import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selectors = DefaultSelector()
MARKET_ENDPOINT = '172.19.60.145'
REQUEST_INFO = 'GET /v2/market/calendar/is_biz_day?date=2020-06-24&region=CN HTTP/1.0\r\n\r\n'
THREAD_NUMBERS = 5


# event loop + call back
class AsyncFirst(object):
    # What would happen to selectors register while raising error in fetch/make_request/read_response

    def __init__(self, thread_id):
        self.thread_id = thread_id
        self.response = []
        self.sock = None
        super().__init__()

    def fetch(self):
        self.sock = socket.socket()
        self.sock.setblocking(False)
        print(self.sock.fileno())
        try:
            self.sock.connect((MARKET_ENDPOINT, 8003))
        except BlockingIOError as ex:
            pass
        # 仅仅是注册(相当于把回调函数和文件fd和事件做了关联绑定， 但是epoll内部是如何判断connect已完成呢？ 因为只有在connect已完成，
        # loop里面的select才会有。难道是不停查询fd,看fd是否有指定的事件(EVENT_WRITE)发生？又或者loop里面的select进行的工作就是不停
        # 查询fd,看fd是否有指定的事件(EVENT_WRITE)发生)
        selectors.register(self.sock.fileno(), EVENT_WRITE, self.make_request)

    def make_request(self, s, event):
        selectors.unregister(s.fd)
        try:
            self.sock.send(REQUEST_INFO.encode('utf-8'))
        except socket.error as ex:
            print(ex)
        selectors.register(s.fd, EVENT_READ, self.read_response)

    def read_response(self, s, event):
        global THREAD_NUMBERS
        d = self.sock.recv(1024)
        if d:
            self.response.append(d.decode('utf-8'))
        else:
            print('{} is Done'.format(self.sock.fileno()))
            print('The result is {}'.format(''.join(self.response)))
            selectors.unregister(s.fd)
            self.sock.close()
            THREAD_NUMBERS -= 1


def loop1():
    while THREAD_NUMBERS:
        events = selectors.select()
        # epoll 内部究竟如何记录事件的信息，仅仅只是记录回调函数的相关信息？
        for event in events:
            callback = event[0].data
            callback(event[0], event[1])


# coroutine, yield from
class Future(object):

    def __init__(self):
        self.result = None
        self._callback = None

    def set_result(self, status):
        self.result = status
        if self._callback:
            self._callback(self)


class Task(object):

    def __init__(self, g):
        self.g = g
        f = Future()
        self.move_forward(f)

    def move_forward(self, future):
        try:
            next_future = self.g.send(future.result)
        except StopIteration:
            return
        next_future._callback = self.move_forward


class AsyncSecond(object):

    def __init__(self):
        self.response = []
        super().__init__()

    def fetch(self):
        sock = socket.socket()
        sock.setblocking(False)
        print(sock.fileno())
        try:
            sock.connect((MARKET_ENDPOINT, 8003))
        except BlockingIOError as ex:
            pass

        f = Future()

        def request_ready():
            f.set_result(None)
            # 实质上执行的是task的move_forward函数 request_ready->set_result->_callback->move_forward
            # 回调函数的作用是驱动协程向前一步,因为协程(生成器)就是由于fetch方法生成的，因为生成器无法直接调用，所以增加future作为中间载体

        selectors.register(sock.fileno(), EVENT_WRITE, request_ready)
        yield f

        selectors.unregister(sock.fileno())
        try:
            sock.send(REQUEST_INFO.encode('utf-8'))
        except socket.error as ex:
            print(ex)

        def read_ready():
            f.set_result(None)
        selectors.register(sock.fileno(), EVENT_READ, read_ready)
        yield f

        global THREAD_NUMBERS
        while True:
            d = sock.recv(1024)
            if d:
                self.response.append(d.decode('utf-8'))
                yield
            else:
                print('{} is Done'.format(sock.fileno()))
                print('The result is {}'.format(''.join(self.response)))
                selectors.unregister(sock.fileno())
                sock.close()
                THREAD_NUMBERS -= 1


def loop2():
    while THREAD_NUMBERS:
        events = selectors.select()
        for event in events:
            callback = event[0].data
            callback(event[0], event[1])


# standard lib : async
class AsyncThird(object):
    pass


if __name__ == '__main__':
    # First Sample
    # for i in range(THREAD_NUMBERS):
    #     thread = AsyncFirst(i)
    #     thread.fetch()
    # loop1()
    # Second Sample
    for i in range(THREAD_NUMBERS):
        thread = AsyncSecond()
        thread.go_forward(thread.fetch())
    loop2()
