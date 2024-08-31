# Assignment: Number Exploration Tool
name = input("Enter your name: ")
num1 = int(input("Enter your 1st favorite number: "))
num2 = int(input("Enter your 2nd favorite number: "))
num3 = int(input("Enter your 3rd favorite number: "))
print(f"Hello, {name}! Let's explore your favorite numbers.")
for num in num1, num2, num3:
        if num % 2 == 0:
            print(f"The number {num} is even")
        else:
            print(f"The number {num} is odd")
for number in num1, num2, num3:
        square = (number, number * number)
        print(f"The number {number} and its square: {square}")

sum = num1 + num2 + num3
print(f"Amazing! The sum of your favorite numbers is: {sum}")
if sum > 1 and sum % 2 != 0: 
        print(f"Wow, {sum} is a prime number!")
else:
    print(f"{sum} is not a prime number.")
