'''Concatenate two lists in the following order by using list comprehension
Input:- list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Output:- [’Hello Dear’, ’Hello Sir’, ’take Dear’, ’take Sir’] '''

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = [f"{x}{y}" for x in list1 for y in list2]
print(result)
