num1 = int(input("Enter 1st Number: ")) 
num2 = int(input("Enter 2nd Number: ")) 
operators = input("Enter Operator (+, -, *, /): ")

if operators == "+":
    print(num1 + num2)
elif operators == "-":
    print(num1 - num2)
elif operators == "*":
    print(num1 * num2)
elif operators == "/":
    # if number is not equal to 0 then use condition otherwise show error
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero.")
else:
    print("Error: Invalid operator.")