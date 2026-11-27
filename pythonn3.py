# Day 03: *args and **kwargs

# 1. Using *args
def add_numbers(*args):
    total = 0

    for num in args:
        total += num

    return total


print("Sum:", add_numbers(10, 20, 30, 40))


# 2. Using **kwargs
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


student_details(
    name="Vikash",
    age=22,
    course="Python",
    city="Bhopal"
)


# 3. Using Both
def student_info(*args, **kwargs):
    print("Subjects:", args)
    print("Details:", kwargs)


student_info(
    "Python",
    "Django",
    "AI",
    name="Vikash",
    age=22
)


# 4. Argument Unpacking
numbers = [10, 20, 30]

print("Unpacked Sum:", add_numbers(*numbers))