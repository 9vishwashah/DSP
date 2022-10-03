n=int(input("enter the no "))
i=1;j=0
while(i<=n):
	while(j<=i-1):
		print("* ",end="")
		j+=1
	print("\r")
	j=0;i+=1
# enter the no 4
# *
# * *
# * * *
# * * * *
