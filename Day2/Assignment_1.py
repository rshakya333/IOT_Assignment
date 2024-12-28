'''Write a function to return simple interest'''

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest per month: "))
t = float(input("Enter the time period in months: "))
def si(p,r,t):
    return (p*r*t)/100
print(f"The simple interest is: {si(p,r,t)}")