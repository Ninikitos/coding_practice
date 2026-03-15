import time

from functools import wraps
from time import perf_counter

def timer(func):
    """
    A decorator that measures how long a function takes to run.
    Useful for spotting slow functions and benchmarking performance
    without modifying the function itself.

    How it works on add_summ(1, 1):
        1. records the start time
        2. calls add_summ(1, 1) sleeps 2 seconds returns 2
        3. records end time and subtracts start
        4. prints  "Total time execution: 2.0001..."
        5. returns 2

    perf_counter() vs time.time() — why perf_counter is better here:
        time.time()        wall clock time, affected by system clock changes
                           (NTP updates, daylight saving, etc.)
        perf_counter()     high resolution timer, only meant for measuring
                           intervals, not affected by clock changes. More precise.
    """
    @wraps(func)
    def decorated_func(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        total_time = perf_counter() - start_time
        print('Total time execution: ', total_time)
        return result
    return decorated_func

@timer
def add_summ(a, b):
    time.sleep(2)
    return a + b

add_summ(1, 1)