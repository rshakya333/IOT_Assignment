# 5)The marks obtained by a student in 3 different subjects are input by the user. 
# Your program should calculate the average of subjects and display the grade. 
# The student gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F

Sub1 = int(input("Enter Marks of Subject 1 "))
Sub2 = int(input("Enter Marks of Subject 2 "))
Sub3 = int(input("Enter Marks of Subject 3 "))

average = (Sub1+Sub2+Sub3)/3

if(average>=90)and(average<=100):
    print(f"Your Average is {average} and you got 'A' Grade")
elif(average>=80)and(average<=89):
    print(f"Your Average is {average} and you got 'B' Grade")
elif(average>=70)and(average<=79):
    print(f"Your Average is {average} and you got 'C' Grade")
elif(average>=60)and(average<=69):
    print(f"Your Average is {average} and you got 'D' Grade")
else:
    print(f"Your Average is {average} and you failed")