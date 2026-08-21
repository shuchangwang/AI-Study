class Test(object):
    def __init__(self, name):
        self.name = name

    def __or__(self, other):
        # return [self, other]
        return MySequence(self, other)

    def __str__(self):
        return self.name


class MySequence(object):
    def __init__(slef, *args):
        slef.sequence = []
        for arg in args:
            slef.sequence.append(arg)

    def __or__(self, other):
        self.sequence.append(other)
        return self

    def run(self):
        for arg in self.sequence:
            print(arg)


if __name__ == "__main__":
    a = Test("a")
    b = Test("b")
    c = Test("c")
    d = a | b | c
    d.run()
    """
    a
    b
    c
    """
    print(type(d))  # <class '__main__.MySequence'>
    print(d)  # <__main__.MySequence object at 0x000001FA080BBA10>
