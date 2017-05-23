class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class StaticData:
    __metaclass__ = Singleton

    i = 123

    @classmethod
    def __call__(cls, *args, **kwargs):
        return cls()

    def next_int(self):
        self.i += 1
        return self.i


i1 = StaticData().next_int()
i2 = StaticData().next_int()
i3 = StaticData().next_int()
i4 = StaticData().next_int()

bp = 0
