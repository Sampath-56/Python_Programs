# Write a Python program to check if a number is binary or not.

num = int(input("Enter a number: "))
is_binary = True

while num > 0:  
    l = num % 10  
     
    if l != 0 and l != 1:  
        print("Given number is not binary")  
        is_binary = False
        break  
     
    num = num // 10  
     
if is_binary:
    print("Given number is binary")  

#Output: Enter a number: 1010
#Given number is binary