number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))

if number1 > number2:
    print(number1, "is larger.")
elif number2 > number1:
    print(number2, "is larger.")
else:
    print("These numbers are equal.")