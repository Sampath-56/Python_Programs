n = int(input("Enter the number of rows: "))
for i in range(n+1):
    for j in range(i):
        print(i,end="")
    print()    

# Output: Enter the number of rows: 5
#         1
#         22
#         333
#         4444
#         55555
