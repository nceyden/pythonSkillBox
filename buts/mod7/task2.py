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

cache = {0: 0, 1: 1}

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

