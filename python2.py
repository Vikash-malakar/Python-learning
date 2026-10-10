import time
from functools import wraps

def execution_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()
        print(f"{func.__name__} executed in {end-start:.6f} seconds")

        return result
    return wrapper


@execution_timer
def process_data(n):
    return sum(i ** 2 for i in range(n))


result = process_data(1_000_000)
print("Result:", result)