import time

def validate_args(func):
    def wrapp(*args):
        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 else "Too many arguments"

        arg = args[0]

        if not isinstance(arg, int):
            return "Wrong types"

        if arg < 0:
            return "Negative argument"

        return func(*args)

    wrapp.__name__ = func.__name__
    wrapp.__doc__ = func.__doc__
    return wrapp

def memoize(func):
    def memoized_func(*args):
        if args[0] not in cache.keys():
            cache[args[0]] = func(args[0])
            return cache[args[0]]
        else:
            return cache[args[0]]

    memoized_func.__name__ = func.__name__
    memoized_func.__doc__ = func.__doc__
    return memoized_func

def timer(func):
    def timed_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Скорость выполнения равна: {end_time - start_time} секунд")
        return result

    timed_func.__name__ = func.__name__
    timed_func.__doc__ = func.__doc__
    return timed_func

cache = {0: 0, 1: 1}

@timer
@validate_args
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

#с memoize
result_with_memoize = fibonacci(10)
cache.clear()
#без memoize
result_without_memoize = fibonacci(10)
