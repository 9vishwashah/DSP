# Write a Python program to reverse a list.
l=[34, 56 , 78, 86]
L = len(l)
for i in range(int(L/2)):
    n = l[i]
    l[i] = l[L-i-1]
    l[L-i-1] = n
print(l)
# OUTPUT 
# [86, 78, 56, 34]
