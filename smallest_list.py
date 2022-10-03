# Write a Python program to get the smallest number from a list.
l=[34, 56 , 78, 86]
m= l[ 0 ]
for a in l:
    if a < m:
            m = a
print("smallest num in list is",m)
# OUTPUT
# smallest num in list is 34
