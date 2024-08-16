n = int(input("Enter the number limit: "))
list = []
for i in range(n):
    num = int(input("Enter the number: "))
    list.append(num)        
print("Original List: ",list)      
s = len(list)
for i in range(s):
    for j in range(0,s-i-1):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
print("Sorted List: ",list)            