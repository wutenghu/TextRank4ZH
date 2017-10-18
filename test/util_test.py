from textrank4zh import util


def test_attr_dict():
    r = util.AttrDict(a=2)
    print(r)
    print(r.a)
    print(r['a'])


def test_combine():
    print(20*'*')
    for item in util.combine(['a', 'b', 'c', 'd'], 2):
        print(item)
    for item in util.combine(['a', 'b', 'c', 'd'], 3):
        print(item)


def test_debug():
    util.debug('你好')
    util.debug(u'世界')


if __name__ == "__main__":
    test_attr_dict()
    test_combine()
    test_debug()
