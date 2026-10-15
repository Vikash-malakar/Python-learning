import sys

def data_generator(limit):
    for number in range(limit):
        yield {
            "id": number,
            "square": number ** 2,
            "cube": number ** 3
        }


def process_records(records):
    for record in records:
        if record["square"] % 2 == 0:
            yield record


records = data_generator(1_000_000)
filtered = process_records(records)

for item in filtered:
    if item["id"] >= 10:
        break
    print(item)

print("Generator memory:", sys.getsizeof(data_generator(1000000)))