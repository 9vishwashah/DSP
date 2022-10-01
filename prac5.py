#1.create a tuple and find min and max num from it
# Smallest
t1=[2, 5, 6, 6, 7, 8, 9]
s=t1[0]
for i in range(len(t1)):
    if (s>t1[i]):
        s=t1[i]
print("the smallest element is",s)
# the smallest element is 2

# Largest
t2=[2, 5, 6, 6, 7, 8, 9]
s=t2[0]
for i in range(len(t2)):
    if (s<t2[i]):
        s=t2[i]
print("the Largest element is",s)
# the Largest element is 9

#2.Write a python program to find repeated items of a tuple 
# t = [int(x) for x in input("Enter any value:").split()]
# t = tuple(t)
t=[2, 5, 6, 6, 7, 8, 9]
print("Repeated Values is:")
for i in range(0,len(t)):
    for j in range(i+1,len(t)):
        if t[i]==t[j]:

            print(t[i])
# OUTPUT
# Repeated Values is:
# 6

#3.Print the number in words
def Value(no):
    if no=='1':
        print("One")
    elif no =='2':
        print("Two")
    elif no =='3':
        print("Three")
    elif no =='4':
        print("Four")
def word(n):
    i=0
    length=len(n)
    while i<length:
        Value(n[i])
        i+=1
n="1234"
word(n)