n=int(input("Enter the number "))
for i in range(n, 0, -2):
    for j in range((n-i) // 2):
        print(" ", end="")
    for j in range(i):
        if j % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()
# Enter the number 9
# 101010101
#  1010101
#   10101
#    101
#     1
