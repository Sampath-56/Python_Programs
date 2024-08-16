def alphabet(n):
    start = 65 
    
    for i in range(n):
        for j in range(i + 1):
            ch = chr(start + j)  
            print(ch, end=" ")
        print("")  

n = 5
alphabet(n)
