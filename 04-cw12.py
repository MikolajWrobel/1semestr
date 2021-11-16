def sum(n):
    if n==1:
        return 1
    
    if n>1:
        return n + sum(n-1)

x = 10
print(sum(x))