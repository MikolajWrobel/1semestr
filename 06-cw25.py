def minmax(array):
    n1=max(array)
    n2=min(array)
    x = [n2,n1]
    return x
    
array = [4,2,8,4,7,9,5]
print(f"Array: {array}")
print(f"Result: {minmax(array)}")