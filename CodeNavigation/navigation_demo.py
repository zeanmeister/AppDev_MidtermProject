class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

def main():
    calc = Calculator()
    x = 10
    y = 5

    print("Addition:", calc.add(x, y))
    print("Subtraction:", calc.subtract(x, y))
    print("Multiplication:", calc.multiply(x, y))
    print("Division:", calc.divide(x, y))

if __name__ == "__main__":
    main()
