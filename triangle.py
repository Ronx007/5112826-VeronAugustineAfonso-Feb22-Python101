def print_triangle(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        print(spaces + "*" * i)

try:
    triangle_size = int(input("Enter the size of the triangle: "))
    if triangle_size <= 0:
        print("Error! Triangle size must be a positive integer.")
    else:
        print_triangle(triangle_size)
except ValueError:
    print("Error! Please enter a valid integer.")

