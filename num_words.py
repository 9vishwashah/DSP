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
