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
