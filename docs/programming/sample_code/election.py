# coding=utf-8
# 3 samples for python async
import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selectors = DefaultSelector()
MARKET_ENDPOINT = 'test-market.aqumon.com'
REQUEST_INFO = 'GET /v2/market/calendar/is_biz_day?date=2020-06-24&region=CN HTTP/1.0\r\n\r\n'
THREAD_NUMBERS = 10


# event loop + call back
class AsyncFirst(object):
    # What would happen to selectors register while raising error in fetch/make_request/read_response

    def __init__(self, thread_id):
        self.thread_id = thread_id
        self.response = []
        super().__init__()

    def fetch(self):
        s = socket.socket()
        s.setblocking(False)
        try:
            s.connect((MARKET_ENDPOINT, 8003))
        except socket.error as ex:
            print(ex)
        selectors.register(s.fileno(), EVENT_WRITE, self.make_request)

    def make_request(self, s, event):
        selectors.unregister(s.fileno())
        try:
            s.sendall(REQUEST_INFO.encode('utf-8'))
        except socket.error as ex:
            print(ex)
        selectors.register(s.fileno(), EVENT_READ, self.read_response)

    def read_response(self, s, event):
        global THREAD_NUMBERS
        d = s.recv(1024)
        if d:
            self.response.append(d)
        else:
            print('{} is Done'.format(s.fileno()))
            print('The result is {}'.format(''.join(self.response)))
            selectors.unregister(s.fileno())
            s.close()
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
    for i in range(THREAD_NUMBERS):
        thread = AsyncFirst(i)
        thread.fetch()
    loop()
