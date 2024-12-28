'''Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:
****
*********
*******'''
def histogram(numbers):
    for number in numbers:
        print("*" * number)

numbers = [4, 9, 7, 8, 1, 2, 3, 5, 6, 10]
histogram(numbers)

