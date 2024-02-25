import random

def sum(a, b):
    return a + b
def sub(a, b):
    return a - b
def multi(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Cannot divide by zero."

def generate_random_number():
    return round(random.uniform(0.1, 10), 2)

functions = [sum, sub, multi, divide]

for i in range(10):
    a = generate_random_number()
    b = generate_random_number()

    selected_function = random.choice(functions)

    result = selected_function(a, b)

    print(f"\nOperation {i+1}:")
    print(f"  {a} {selected_function.__name__} {b} = {round(result, 2)}")
