n = int(input("Enter the number of rows: "))
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

# Output: Enter the number of rows: 5
#        1
#        12
#        123
#        1234
#        12345    