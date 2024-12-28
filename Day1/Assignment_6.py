# 6) Write a Python function to calculate the factorial of a number (a non-negative integer). The function acc
# epts the number as an argument.

n = int(input("Enter a number: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f"The factorial of {n} is {factorial(n)}")