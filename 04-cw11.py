def factorial(n):
    if n==0 or n==1:
        return 1
    
    if n>1:
        return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"{n}! = {factorial(n)}")