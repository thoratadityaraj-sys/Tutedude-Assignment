
#1 Take two numbers as input from the user.
#We use float to allow decimal inputs.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#2 Performs the basic arithmetic operations.
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (cannot divide by zero)"
#3 Display the results.
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")



