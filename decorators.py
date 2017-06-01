# There are two ways to implement decorators: class & function

# region Decorator Class
# TODO: Skipped for now because this is less used.
# endregion


# region Decorator Function

def decorator_without_params(f):
    def g(*args):
        print "Start"
        f(*args)
        print "End"
    return g


@decorator_without_params
def func1(x):
    print x

func1("x")
# Should print:
#   Start
#   x
#   End


def decorator_with_params(arg1, arg2):
    def wrapper(f):
        def g(*args):
            print "Start " + arg1
            f(*args)
            print "End " + arg2
        return g
    return wrapper


@decorator_with_params("1", "2")
def func2(x):
    print x

func2("x")
# Should print:
#   Start 1
#   x
#   End 2

# endregion
