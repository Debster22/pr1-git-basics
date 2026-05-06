def sum_numbers(a, b):
    try:
        return a + b
    except TypeError:
        print("Error: arguments must be numbers")
        return None

print("Sum:", sum_numbers(2, 3))
