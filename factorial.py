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
