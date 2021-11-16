def bubblesort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
                
array1 = [5,5,7,2,1]
print(bubblesort(array1))

array2 = [1,4,67,3,1,5,7,2]
print(bubblesort(array2))

array3 = [7,74,8,13,6,2,4,7,1]
print(bubblesort(array3))