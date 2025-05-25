
operator = input("Enter your operator(+,-,/,*): ")
num1= float(input("Enter #num1: "))
num2= float(input("Enter #num2: "))

if operator == "+":
    print(f"Your answer is: {round(num1 + num2,2)}")
elif operator == "-":
    print(f"Your answer is: {round(num1 - num2,2)}")
elif operator == "/":
    print(f"Your answer is: {round(num1 / num2,2)}")
elif operator == "*":
    print(f"Your answer is: {round(num1 * num2,2)}")
else:
    print(f"Enter right operator.")