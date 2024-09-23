def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b
def modulus(a, b):
    return a % b

def calculator():
    print("Select an operation:")
    choice = input("Enter choice (add,sub,mul,div,mod): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 'add':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == 'sub':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == 'mul':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == 'div':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == 'mod':
        print(f"{num1} % {num2} = {modulus(num1, num2)}")
    else:
        print("Invalid input, please select a valid operation.")
calculator()
