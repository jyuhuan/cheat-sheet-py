from abc import ABCMeta, abstractmethod


class Iterator:

    __metaclass__ = ABCMeta

    @abstractmethod
    def advance(self): pass

    @abstractmethod
    def current(self): pass


class ConcreteIterator(Iterator):
    i = 0
    n = 0

    def __init__(self, length):
        self.n = length

    def advance(self):
        self.i += 1
        return self.i < self.n

    def current(self):
        return self.i


it = ConcreteIterator(10)
while it.advance():
    print it.current()
