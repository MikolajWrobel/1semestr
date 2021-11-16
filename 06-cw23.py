def median(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    if n%2>0:
        return array[n//2]
    if n%2==0:
        n1=array[(n//2)-1]
        n2=array[(n//2)]
        return (n1+n2)/2

print(f"a. [1,0,9,4,6] Median: {median([1,0,9,4,6])}")
print(f"b. [6,8,3,1,0,5,7] Median: {median([6,8,3,1,0,5,7])}")
    