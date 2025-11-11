def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


# Example usage
num1 = 10
num2 = 5

print("Basic Calculator")
print(f"Add: {add(num1, num2)}")
print(f"Subtract: {subtract(num1, num2)}")
print(f"Multiply: {multiply(num1, num2)}")
print(f"Divide: {divide(num1, num2)}")
