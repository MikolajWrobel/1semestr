array = [4,3,7,1,3]
def summ(array):
    n = 0
    for i in array:
        n = n+i
    return n

def array2str(array):
    result=''
    for i in array:
        result +=""+str(i)
    return result

print("Array: ",array2str(array))
print("Sum of values: ",summ(array))

    