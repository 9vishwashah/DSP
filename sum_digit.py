# 7.Write a Python program takes in a number and finds the sum of digits in a number.
n=int(input("Enter a number:"))
total=0
while(n>0):
    digit=n%10
    total=total+digit
    n=n//10
print("The total sum of digits is:",total)
# OUTPUT
# Enter a number:23
# The total sum of digits is: 5
