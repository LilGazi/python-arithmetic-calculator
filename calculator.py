def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


calculate = input("Enter arithmetic operation +, -, *, /: ")

if calculate == "+":
    x = float(input("Enter number: "))
    y = float(input("Enter number: "))
    result = add(x, y)
    print("Result:", result)

elif calculate == "-":
    x = float(input("Enter number: "))
    y = float(input("Enter number: "))
    result = subtract(x, y)
    print("Result:", result)

elif calculate == "*":
    x = float(input("Enter number: "))
    y = float(input("Enter number: "))
    result = multiply(x, y)
    print("Result:", result)

elif calculate == "/":
    x = float(input("Enter number: "))
    y = float(input("Enter number: "))
    result = divide(x, y)
    print("Result:", result)

else:
    print("Invalid operation.")
