x=int(input("Enter the dog's age in human years: "))
if x<=2:
    print("The dog's age in dog's years is:",int(10.5*x))
else:
    print("The dog's age in dog's years is",int(10.5*2+(x-2)*4),"years")