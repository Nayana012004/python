def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num=int(input("enter a number: "))
if num < 0:
    print("factorial does not exist for negative numbers")
else:
    print(f"the factorial of {num} is {factorial(num)}")