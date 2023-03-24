number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))

if number1 % number2 == 0:
    print(number1, "is a multiple of", number2)
else:
    print(number1, "is not a multiple of", number2)