# 1.Print the following patterns using loop:

# A)
n=int(input("enter the no "))
i=1;j=0
while(i<=n):
	while(j<=i-1):
		print("* ",end="")
		j+=1
	print("\r")
	j=0;i+=1
# enter the no 4
# *
# * *
# * * *
# * * * *

# B)
rows = 2
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
k = rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
#   * 
#  * *
# * * *
#  * *
#   *

# C)
n=int(input("Enter the number "))
for i in range(n, 0, -2):
    for j in range((n-i) // 2):
        print(" ", end="")
    for j in range(i):
        if j % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()
# Enter the number 9
# 101010101
#  1010101
#   10101
#    101
#     1

# 2.Write a Python program to print all even numbers between 1 to 100 using while loop.
num = 2
while num <= 100:
    print(num)
    num = num + 2
# OUTPUT
# 2
# 4
# 6
# 8
# 10 .... 100

# 3.Write a Python program to find the sum of first 10 natural numbers using for loop.
n=10
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print(f"{sum1} is The sum of first 10 natural numbers")
# OUTPUT
# 55 is The sum of first 10 natural numbers

# 4.Write a Python program to print Fibonacci series.
n_terms = int(input ("How many terms the user wants to print? "))  
n_1 = 0  
n_2 = 1  
count = 0    
if n_terms == 1:  
    print ("The Fibonacci sequence of the numbers up to", n_terms, ": ")  
    print(n_1)    
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < n_terms:  
        print(n_1)  
        nth = n_1 + n_2   
        n_1 = n_2  
        n_2 = nth  
        count += 1  
# OUTPUT
# How many terms the user wants to print? 5
# The fibonacci sequence of the numbers is:
# 0
# 1
# 1
# 2
# 3

# 5.Write a Python program to calculate factorial of a number
num = int(input("Enter a number: "))    
factorial = 1    
if num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)    
# OUTPUT
# Enter a number: 6
# The factorial of 6 is 720

# 6.Write a Python Program to Reverse a Given Number
n = 4562
rev = 0
while(n > 0):
	a = n % 10
	rev = rev * 10 + a
	n = n // 10
print(rev)
# OUTPUT
# 2654

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

# 8.Write a Python program that takes a number and checks whether it is a palindrome or not.
number = int(input("Enter the number: "))
temp = number
reverse =0
while (number > 0):
    dig = number % 10
    reverse = reverse * 10 + dig
    number = number // 10
print("The reverse number is: ", reverse)
if temp==reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")  
# OUTPUT
# Enter the number: 231
# The reverse number is:  132
# The number is not a palindrome

# 9.Write a program to check whether a number is even or odd
n = int(input("Enter the number: "))
if n%2==0:
    print("f{n} is a even number")
else:
    print(f"{n} is a odd number")
# OUTPUT
# Enter the number: 23
# 23 is a odd number

# 10.Write a program to find out absolute value of an input number
a=int(input("Enter the number"))
if a >= 0:
    print(a)
else:
    print(-a)
# OUTPUT
# Enter the number-9
# 9

# 11.Write a program to check the largest number among the three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
print("The largest number is",largest)

# OUTPUT
# Enter first number: 25
# Enter second number: 36
# Enter third number: 10
# The largest number is 36.0

# 12.Write a program to check if the input year is a leap year of not
# Python program to check leap year or not
def checkYear(year):
	if (year % 4) == 0:
		if (year % 100) == 0:
			if (year % 400) == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False
year = int(input("Enter the year"))
if(checkYear(year)):
	print("Leap Year")
else:
	print("Not a Leap Year")
	

# 13.Write a program to check if a Number is Positive, Negative or Zero
n=int(input("Enter a number "))
if n>0:
    print("the number is positive")
elif n<0:
   print("the number is negative")
else:
    print("the number is zero") 
#OUTPUT
# Enter a number 15
# the number is positive

# 14.Write a program that takes the marks of 5 subjects and displays the grade.
sub1=float(input("Enter marks of the first subject: "))
sub2=float(input("Enter marks of the second subject: "))
sub3=float(input("Enter marks of the third subject: "))
sub4=float(input("Enter marks of the fourth subject: "))
sub5=float(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
else:
    print("Grade: F")
# OUTPUT
# Enter marks of the first subject: 54
# Enter marks of the second subject: 46
# Enter marks of the third subject: 32
# Enter marks of the fourth subject: 15
# Enter marks of the fifth subject: 21
# Grade: F