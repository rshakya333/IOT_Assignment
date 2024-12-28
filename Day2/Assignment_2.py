'''Write a function to return compound interest'''

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest per annum: "))
t = float(input("Enter the time period in years: "))
n = float(input("Enter the number of times interest is compounded per year: "))

def ci(p, r, t, n):
    amount = p * (1 + r/(n * 100))**(n * t)
    ci = amount - p  # Calculate the compound interest
    return ci

print(f"The Compound interest is: {ci(p, r, t, n)}")

