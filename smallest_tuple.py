#1.create a tuple and find min and max num from it
# Smallest
t1=[2, 5, 6, 6, 7, 8, 9]
s=t1[0]
for i in range(len(t1)):
    if (s>t1[i]):
        s=t1[i]
print("the smallest element is",s)
# the smallest element is 2
