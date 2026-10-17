import asyncio
import time

async def fetch_data(api_name, delay):
    print(f"Fetching {api_name}...")

    await asyncio.sleep(delay)

    return {
        "api": api_name,
        "status": "success",
        "response_time": delay
    }


async def main():
    start = time.perf_counter()

    tasks = [
        fetch_data("Users API", 2),
        fetch_data("Products API", 3),
        fetch_data("Orders API", 1)
    ]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

    print("Total time:", round(time.perf_counter() - start, 2))


if __name__ == "__main__":
    asyncio.run(main())