number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter the operation to perform (add, subtract, multiply, divide): ")

if operation == "add":
    answer = number1 + number2
elif operation == "subtract":
    answer = number1 - number2
elif operation == "multiply":
    answer = number1 * number2
elif operation == "divide":
    answer = number1 / number2
else:
    print("Invalid operation entered.")
    exit()

print("The result is:", answer)