import numpy as np

employee_dtype = [
    ("id", "i4"),
    ("name", "U20"),
    ("department", "U15"),
    ("salary", "f8")
]

employees = np.array([
    (101, "Vikash", "IT", 45000),
    (102, "Aman", "HR", 35000),
    (103, "Rahul", "IT", 55000),
    (104, "Priya", "Finance", 60000),
    (105, "Neha", "IT", 50000)
], dtype=employee_dtype)

# Filter IT employees
it_employees = employees[
    employees["department"] == "IT"
]

# Salary analysis
average_salary = np.mean(employees["salary"])

# Sort by salary
sorted_employees = np.sort(
    employees,
    order="salary"
)

print("IT Employees:\n", it_employees)
print("\nAverage Salary:", average_salary)
print("\nSorted Employees:\n", sorted_employees)