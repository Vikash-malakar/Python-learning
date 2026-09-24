import time


def stopwatch():
    print("\n" + "=" * 40)
    print("             ⏱️ STOPWATCH")
    print("=" * 40)

    input("\nPress ENTER to start...")

    start_time = time.time()

    print("⏳ Stopwatch running...")
    print("Press ENTER to stop.")

    input()

    end_time = time.time()

    elapsed = end_time - start_time

    print(f"\n⏱️ Time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    stopwatch()