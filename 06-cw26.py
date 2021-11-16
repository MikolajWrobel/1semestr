array = [1,6,3,5,2,8,4]
n = len(array)
for i in range(n-1):
    for j in range(0,n-i-1):
        if array[j]%2>0:
            array[j], array[j+1] = array[j+1], array[j]
            
print(array)
        