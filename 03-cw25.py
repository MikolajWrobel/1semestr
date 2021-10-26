b=int(input("Length: "))
a=int(input("Width: "))

if b<3:
    print("*"*b)
    for a in range(a-1):
        print("*"*b)
elif a==1:
    print("*"*b)
elif b==3:
    print("*"*b)
    for a in range (a-2):
        print("*","*")
    print("*"*b)
else:
    print("*"*b)
    for a in range (a-2):
        print("*",' '*(b-4),"*")
    print("*"*b)