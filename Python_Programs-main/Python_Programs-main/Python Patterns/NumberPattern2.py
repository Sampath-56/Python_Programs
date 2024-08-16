n = int(input("Enter the number of rows: "))
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()    

# Output: Enter the number of rows: 5
#         12345
#         1234
#         123
#         12
#         1
