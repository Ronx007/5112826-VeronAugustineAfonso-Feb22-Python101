def sum_func(a, b):
    return a + b

def sub_func(a, b):
    return a - b

def multi_func(a, b):
    return a * b

def divide_func(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."

# Perform 10 operations
operations = [
    (5, 2),
    (10.5, 3.2),
    (8, 4),
    (15.7, 2.5),
    (20, 0),
    (6.3, 2),
    (12, 3),
    (18.6, 2.3),
    (9, 0.5),
    (14, 7)
]

for i, (a, b) in enumerate(operations, start=1):
    result_sum = sum_func(a, b)
    result_sub = sub_func(a, b)
    result_multi = multi_func(a, b)
    result_divide = divide_func(a, b)

    print(f"\nOperation {i}:")
    print(f"  {a} + {b} = {result_sum}")
    print(f"  {a} - {b} = {result_sub}")
    print(f"  {a} * {b} = {result_multi}")
    print(f"  {a} / {b} = {result_divide}")

