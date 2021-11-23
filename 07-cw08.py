f = open("countries.txt","r")
x=1
for line in f:
    print(f"{x}.{line}",end='')
    x+=1