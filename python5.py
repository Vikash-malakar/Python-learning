from concurrent.futures import ProcessPoolExecutor
import time

def calculate_square(number):
    return number ** 2

def main():
    numbers = range(1, 100001)

    start = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(calculate_square, numbers))

    print("Total results:", len(results))
    print("First 10:", results[:10])
    print("Execution time:",
          round(time.perf_counter() - start, 3), "seconds")


if __name__ == "__main__":
    main()