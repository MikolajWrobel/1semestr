f = open("numbers.txt","r")
z=0
for x in f:
    z=z+int(x)
    
print(z)