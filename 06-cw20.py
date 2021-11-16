def occurs(number,array):
    w=0
    x=0
    while w<=len(array):
        if number==array[x]:
            return True
        else:
            w+=1
            x+=1
        if w==len(array):
            return False 
        
number = int(input("Enter a number: "))
array  = [15,38,7,23,14]

z=''
for x in range(len(array)):
    z=f"{z} {array[x]}"
    
print(f"Number: {number}")
print(f"Array:{z}")
if occurs(number,array)==True:
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} do not appear in the array")