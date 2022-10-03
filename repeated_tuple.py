#2.Write a python program to find repeated items of a tuple 
t=[2, 5, 6, 6, 7, 8, 9]
print("Repeated Values is:")
for i in range(0,len(t)):
    for j in range(i+1,len(t)):
        if t[i]==t[j]:

            print(t[i])
# OUTPUT
# Repeated Values is:
# 6
