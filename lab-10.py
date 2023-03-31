def calculate_average(N):
    sum = 0
    for i in range(1, N+1):
        sum += i
    average = sum / N
    return average

N = int(input("Enter an integer greater than 1: "))

result = calculate_average(N)

print("The average of integers from 1 to", N, "is:", result)