# 7) Using for loop, write and run a Python program to find factorial from 0 to 10.

for var in range(0,11):
    i = 1
    fact = 1
    while i <= var:
        fact = fact * i
        i = i + 1
    print(f"Factorial of {var} = {fact}")

