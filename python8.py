from functools import lru_cache
import time


@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


start = time.perf_counter()

result = fibonacci(500)

print("Fibonacci result:", result)
print("Execution time:", time.perf_counter() - start)

print("Cache Information:")
print(fibonacci.cache_info())

# Clear cached results
fibonacci.cache_clear()
print("Cache cleared!")