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
