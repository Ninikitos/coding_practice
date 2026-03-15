from functools import wraps

def trace(func):
    """
    A decorator that logs what a function was called with and what it returned.
    Useful for debugging. Add @trace on any function and instantly
    see what's going in and coming out without touching the function itself.

    How it works on say('Nick', 'Hello'):
        1. prints  "TRACE: calling say() with args: ('Nick', 'Hello') and kwargs: {}"
        2. calls the original say('Nick', 'Hello') → returns 'Nick, Hello!'
        3. prints  "TRACE: say() returned 'Nick, Hello!'"
        4. returns 'Nick, Hello!'

    The !r in the f-string:
        {orig_result!r} prints the REPR of the value instead of just the string.
        This means strings show up with their quotes, so you can tell the
        difference between a string and a number.
    """
    @wraps(func)
    def decorated_func(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with args: {args} and kwargs: {kwargs}')
        orig_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() '
              f'returned {orig_result!r}')
        return orig_result
    return decorated_func

@trace
def say(name, greet):
    return f'{name}, {greet}!'

say('Nick', 'Hello')