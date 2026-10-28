import numpy as np
import time

rng = np.random.default_rng(42)

data = rng.integers(1, 100, size=1_000_000)

# Traditional Python approach
start = time.perf_counter()

python_result = [
    x * 2 + 10
    for x in data
]

python_time = time.perf_counter() - start

# NumPy vectorized approach
start = time.perf_counter()

numpy_result = data * 2 + 10

numpy_time = time.perf_counter() - start

print("Python Time:", python_time)
print("NumPy Time:", numpy_time)

if numpy_time > 0:
    print("Speedup:", python_time / numpy_time)