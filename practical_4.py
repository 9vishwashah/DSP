# Write a Python program to sum all the items in a list.
l=[34, 56 , 78, 86]
total=0
for i in l:
    total=total+i
print(total)
# OUTPUT
# 254
# Write a Python program to multiply all the items in a list.
l=[34, 56 , 78, 86]
total=1
for i in l:
    total*=i
print(total)
# OUTPUT
# 12772032

# Write a Python program to get the largest number from a list.
l=[34, 56 , 78, 86]
m= l[ 0 ]
for a in l:
    if a > m:
            m = a
print("max num in list is",m)
# OUTPUT
# max num in list is 86

# Write a Python program to get the smallest number from a list.
l=[34, 56 , 78, 86]
m= l[ 0 ]
for a in l:
    if a < m:
            m = a
print("smallest num in list is",m)
# OUTPUT
# smallest num in list is 34

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

# Write a Python program to find common items from two lists.
l1 = [5, 10, 15, 20, 25, 30]
l2= [10, 20, 30, 40, 50, 60]
common_list = [c for c in l1 if c in l2]
print(common_list)
# OUTPUT
# [10, 20, 30]
