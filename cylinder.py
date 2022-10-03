# 6.Write a program to calculate surface volume and area of a cylinder.
pi= 3.14
radius = float(input('Please Enter the Radius of a Cylinder: '))
height = float(input('Please Enter the Height of a Cylinder: '))
sa = 2 * pi * radius * (radius + height)
Volume = pi * radius * radius * height
print(f"{sa} is Surface area of a Cylinder")
print(f"{Volume} is Volume of a Cylinder")
#OUTPUT
# Please Enter the Radius of a Cylinder: 5
# Please Enter the Height of a Cylinder: 5
# 314.0is Surface area of a Cylinder
# 392.5is Volume of a Cylinder
