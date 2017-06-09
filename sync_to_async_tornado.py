# Consider a blocking method like this:


def slow_func():
    i = 0
    for x in range(6000000):
        i += 1
    return i

# We don't want to call it directly as follows
result = slow_func()

# Using Tornado and Python's concurrent library,
# we can convert it to an async function.

# Import these first:
from tornado.concurrent import Future, run_on_executor
from concurrent.futures import ThreadPoolExecutor


class MyFuncs:
    executor = ThreadPoolExecutor(max_workers=4)

    @run_on_executor
    def slow_func(self):
        i = 0
        for x in range(6000000):
            i += 1
        return i

# Now this function becomes async, and returns a Future
my_funcs = MyFuncs()
fut = my_funcs.slow_func()


def callback(x):
    print x.result()

fut.add_done_callback(callback)
