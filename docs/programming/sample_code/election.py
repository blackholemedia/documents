# coding=utf-8
# 3 samples for python async
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


def loop():
    while THREAD_NUMBERS:
        events = selectors.select()
        for event in events:
            callback = event[0].data
            callback(event[0], event[1])


# coroutine, yield from
class AsyncSecond(object):
    pass


# standard lib : async
class AsyncThird(object):
    pass


if __name__ == '__main__':
    # First Sample
    for i in range(THREAD_NUMBERS):
        thread = AsyncFirst(i)
        thread.fetch()
    loop()
