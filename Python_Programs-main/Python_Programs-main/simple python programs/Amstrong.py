num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"Armstrong number")
else:
   print(num,"not Armstrong number")

# Amstrong number examples : 0,1,407,370,etc..   