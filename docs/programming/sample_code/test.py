def s():
    f = 12
    yield f
    print('start')
    m = yield 5
    print('m is ' + m)
    d = yield 16
    print('go on!')


if __name__ == '__main__':
    c = s()
    s_1 = c.send(None)
    print('1st')
    s_2 = c.send('hhahhhhha')
    print('2nd')
    s_3 = c.send('fuck')
    print('3rd')
    print(s_1, s_2)
