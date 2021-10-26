z=0
n=int(input("Enter an amount of prime numbers: "))
for x in range(2,n**n):
    y=2
    if z!=n:
        while y <= x**0.5:
            if x % y == 0:
                break
            y+=1
        else:
            print(x)
            z+=1
    else:
        break
            
                
            
        
    
        
        