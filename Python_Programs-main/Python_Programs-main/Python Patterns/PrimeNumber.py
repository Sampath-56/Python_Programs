n = int(input("Enter the number: "))
a = int(n/2)+1
for i in range(2,a):
    r = n%i
    if r == 0:
        print(n,"Not Prime")
        break
else:
    print(n,"Prime")