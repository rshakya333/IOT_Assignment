# 3] Write a program to accept three integer numbers and find its average.
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))

def ave(num1: float, num2: float, num3: float):
    return (num1 + num2 + num3) / 3
print(f"The Average of the three numbers is: {ave(num1,num2,num3)}")