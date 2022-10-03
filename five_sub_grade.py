# 14.Write a program that takes the marks of 5 subjects and displays the grade.
sub1=float(input("Enter marks of the first subject: "))
sub2=float(input("Enter marks of the second subject: "))
sub3=float(input("Enter marks of the third subject: "))
sub4=float(input("Enter marks of the fourth subject: "))
sub5=float(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
else:
    print("Grade: F")
# OUTPUT
# Enter marks of the first subject: 54
# Enter marks of the second subject: 46
# Enter marks of the third subject: 32
# Enter marks of the fourth subject: 15
# Enter marks of the fifth subject: 21
# Grade: F
