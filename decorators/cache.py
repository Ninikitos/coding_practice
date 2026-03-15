from functools import wraps

def args_cache(func):
    """
    A decorator that remembers the results of previous calls so it doesn't
    have to recalculate the same thing twice. This is called memoization.

    Uses a dictionary where:
        key   - the arguments you called the function with - (1, 1)
        value - the result that was returned               - 2

    How it works on add_summ(1, 1) called twice:
        call 1: (1,1) not in values - calculate - store values[(1,1)] = 2 - return 2
        call 2: (1,1) IS in values  - return values[(1,1)] = 2, skip calculation ✅

    Output:
        add_summ(1, 1)  # Calculating....        - 2  (first time, does the work)
        add_summ(1, 1)  # Returning from cache 2 - 2  (second time, free!)
        add_summ(1, 2)  # Calculating....        - 3  (new args, does the work)
        add_summ(1, 2)  # Returning from cache 3 - 3  (seen before, free!)

    Why args works as a dictionary key:
        args comes in as a TUPLE - tuples are immutable so they can be hashed,
        which means they can be used as dictionary keys. Lists can't do this.

        values[(1, 1)] = 2    # ✅ tuple as key, works fine
        values[[1, 1]] = 2    # ❌ list as key, crashes — TypeError: unhashable type

    Real world use case — expensive calculations:
        @cache
        def fibonacci(n):
            if n <= 1:
                return n
            return fibonacci(n-1) + fibonacci(n-2)

        fibonacci(10) - calculates everything from scratch
        fibonacci(10) - instant, pulled from cache
        fibonacci(8)  - instant too! was already calculated on the way to 10

    One limitation — kwargs aren't cached here:
        add_summ(1, 1)     - cached, args=(1,1)
        add_summ(a=1, b=1) - not cached, kwargs aren't included in the key
    """
    values = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in values:
            print(f'Value {values[args]} was returned from cache', )
            return values[args]
        print(f'Calculating....')
        values[args] = func(*args, **kwargs)
        return values[args]
    return wrapper

@args_cache
def add_summ(a, b):
    print(f'{add_summ.__name__} call')
    return a + b

add_summ(1, 1)
add_summ(1, 1)
add_summ(1, 3)
add_summ(1, 2)
