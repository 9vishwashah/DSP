# 1.Write a program to convert U.S. dollars to Indian rupees.
usd = float(input("Enter currency in USD: "))
inr = usd * 81.58
print("The currency in INR is",round(inr,2))
# OUTPUT
# Enter currency in USD: 44
# The currency in INR is 3589.52
# 2.Write a program to convert bits to Megabytes, Gigabytes and Terabytes
def convert_bytes(bytes_number):
    tags = [ "Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte" ]
    i = 0
    double_bytes = bytes_number
    while (i < len(tags) and  bytes_number >= 1024):
            double_bytes = bytes_number / 1024.0
            i = i + 1
            bytes_number = bytes_number / 1024
    return str(round(double_bytes, 2)) + " " + tags[i] 
print(convert_bytes(4896587482345))
print(convert_bytes(9876524362))
print(convert_bytes(10248000))
# OUTPUT
# 4.45 Terabyte
# 9.2 Gigabyte
# 9.77 Megabyte
