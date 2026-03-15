from functools import wraps

def retry(n):
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(f'attempt {attempt + 1} failed: {e}')
            raise last_error
        return inner_wrapper
    return outer_wrapper

count = 0

@retry(3)
def flaky_function():
    global count
    count += 1
    if count < 3:
        raise ValueError(f'failed on attempt {count}')
    return 'success!'

print(flaky_function())