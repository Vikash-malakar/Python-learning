from functools import reduce

transactions = [
    {"user": "A", "amount": 1200, "status": "success"},
    {"user": "B", "amount": 800, "status": "failed"},
    {"user": "C", "amount": 2500, "status": "success"},
    {"user": "A", "amount": 700, "status": "success"},
    {"user": "D", "amount": 1500, "status": "failed"},
]

successful = list(filter(
    lambda x: x["status"] == "success",
    transactions
))

amounts = list(map(
    lambda x: x["amount"],
    successful
))

total_revenue = reduce(
    lambda total, amount: total + amount,
    amounts,
    0
)

print("Successful Transactions:", successful)
print("Amounts:", amounts)
print("Total Revenue:", total_revenue)