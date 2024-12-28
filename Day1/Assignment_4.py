# 4] Write a Python function to find the maximum of three numbers.

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))
max = 0
if num1 >= num2 and num1 >= num3:
        max = num1
elif num2 >= num1 and num2 >= num3:
        max = num2
else:
    max = num3
print(f"Max of the numbers {num1},{num2},{num3} = {max}")
 
    
        