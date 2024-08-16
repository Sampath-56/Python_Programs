ch = str(input("Enter the character: "))
a = ord(ch)
for i in range(65,a+1):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()