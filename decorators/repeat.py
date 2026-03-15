import functools

def repeat(x):
    """
    A decorator factory that runs a function x times and returns the last result.

    Called a 'factory' because repeat(3) doesn't decorate anything yet —
    it just BUILDS and returns the decorator with 3 locked in.
    The actual decorating happens in outer_func.

    3 layers each has one job:
        repeat(x)           catches the argument (how many times to run)
        outer_func(func)    catches the function to decorate
        inner_func(...)     the actual wrapper that runs when you call add_summ()

    What happens when you call add_summ(1, 1):
        1. inner_func receives args=(1, 1)
        2. result = None, safe default in case x=0
        3. loops 3 times, each time calling add_summ(1, 1)
            → prints 'add_summ call'
            → result = 2
        4. returns 2 (the last result)

    Output:
        add_summ call   # run 1
        add_summ call   # run 2
        add_summ call   # run 3
    """
    def outer_func(func):
        @functools.wraps(func)
        def inner_func(*args, **kwargs):
            result = None
            for _ in range(x):
                result = func(*args, **kwargs)
            return result
        return inner_func
    return outer_func

@repeat(3)
def add_summ(a, b):
    print(f'{add_summ.__name__} call')
    return a + b

add_summ(1, 1)