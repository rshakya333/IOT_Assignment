'''Find and display the largest number of a list without using built-in function max(). Your program should
ask the user to input values in list from keyboard.'''

list1 = []
num = int(input("Enter the number of elements in the list: "))
for i in range(0, num):
    ele = int(input())
    list1.append(ele)

largest = list1[0]
for i in range(1, len(list1)):
    if list1[i] > largest:
        largest = list1[i]

print("Largest element is:", largest)
