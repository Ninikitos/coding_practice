from functools import wraps

def uppercase(func):
    """
    A decorator that wraps a function and uppercases its return value.

    A decorator is just a function that takes another function, wraps some
    extra behavior around it, and returns the wrapped version. Think of it
    like gift wrapping. The original function is still in there, you just
    added a layer around it.

    How it works step by step:
        @uppercase applied to greet() means Python does this behind the scenes:
            greet = uppercase(greet)
        So every time you call greet(), you're actually calling decorated_func()

    What happens when you call greet():
        1. prints  'before func'
        2. calls the ORIGINAL greet() → prints '- calling greet -', returns 'hello'
        3. prints  'after func'
        4. uppercases 'hello' → 'HELLO'
        5. returns 'HELLO'

    Output:
        before func
        - calling greet -
        after func
        HELLO

    *args and **kwargs — why they're here:
        decorated_func doesn't know what arguments the original function needs,
        so it just accepts everything and passes it through. This makes the
        decorator reusable on any function regardless of its signature.

        @uppercase
        def greet(name):           # now greet takes an argument
            return f'hello {name}'

        greet('alice')             # 'HELLO ALICE'  still works fine

    @wraps(func) — why it's there:
        Without it, greet.__name__ would return 'decorated_func' instead of 'greet'
        because you replaced greet with the wrapper. @wraps copies the original
        function's metadata (name, docstring) onto the wrapper so it still
        LOOKS like the original from the outside.

        without @wraps:  greet.__name__  - 'decorated_func'  - confusing
        with @wraps:     greet.__name__  - 'greet'           - correct
    """
    @wraps(func)
    def decorated_func(*args, **kwargs):
        print('before func')
        orig_result = func(*args, **kwargs)
        print('after func')
        uppercase_result = orig_result.upper()
        return uppercase_result
    return decorated_func


@uppercase
def greet():
    print('- calling greet - ')
    return 'hello'

print(greet())