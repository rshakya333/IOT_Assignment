# Write a program to accept a 4 digit number and
# a. Display face value of each decimal digit
# b. Display place value of each decimal digit
# c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 outp
# ut should be
# a. 9 3 6 1
# b. 9361 = 9 000 + 300 + 60 + 9
# c. 1639

Num = int(input("Enter Any four Digit Number: "))
main = Num

D4 = int(Num%10)
Num = int(Num/10)

D3 = int(Num%10)
Num = int (Num/10)

D2 = int(Num%10)
Num = int(Num/10)

D1 = int(Num%10)
Num = int(Num/10)

print(f"Face Value : {D1} : {D2} : {D3} : {D4}")
print(f"Place Value {main}:{D1*1000}+{D2*100}+{D3*10}+{D4}")
print(f"Reverse Number : {D4*1000+D3*100+D2*10+D1}")