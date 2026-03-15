import time
from functools import wraps

def rate_limit(calls: int, period: int):
    def outer_wrapper(func):
        call_time = []
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            curr_time = time.time()
            call_time[:] = [t for t in call_time if t > curr_time - period]
            if len(call_time) >= calls:
                raise RuntimeError(f'Wait {period}s before calling {func.__name__} again')
            else:
                call_time.append(curr_time)
                return func(*args, **kwargs)
        return inner_wrapper
    return outer_wrapper

@rate_limit(2, 1)
def add_nums(a: int, b: int) -> int:
    return a + b

for i in range(5):
    try:
        print(f'call {i+1}:', add_nums(1, 1))
    except RuntimeError as e:
        print(f'call {i+1} blocked:', e)