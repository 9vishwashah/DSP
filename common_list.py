# Write a Python program to find common items from two lists.
l1 = [5, 10, 15, 20, 25, 30]
l2= [10, 20, 30, 40, 50, 60]
common_list = [c for c in l1 if c in l2]
print(common_list)
# OUTPUT
# [10, 20, 30]
