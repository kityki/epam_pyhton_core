import time
from typing import Dict

execution_time: Dict[str, float] = {}

def time_decorator(func):
    from time import time
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        #t2 = time()
        end = time() - t1
        execution_time[func.__name__] = end
        return result

    return wrapper

@time_decorator
def func_add(a, b):
    time.sleep(0.2)
    return a + b
