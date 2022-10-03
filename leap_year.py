# 12.Write a program to check if the input year is a leap year of not
# Python program to check leap year or not
def checkYear(year):
	if (year % 4) == 0:
		if (year % 100) == 0:
			if (year % 400) == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False
year = int(input("Enter the year"))
if(checkYear(year)):
	print("Leap Year")
else:
	print("Not a Leap Year")
	
