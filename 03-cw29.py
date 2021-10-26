sum=0
for x in range(0,10000000):
    y=int(input("Enter a number: "))
    sum=sum+y
    if y==0:
        break
print(f"RESULT: Quantiny = {x}, Sum = {sum}, Mean = {sum/x}")
