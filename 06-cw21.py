def bubblesort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

numbers = [5,1,9,6,1]
print(f"Array: {numbers}")

bubblesort(numbers)
print(f"Result: {numbers[len(numbers)-2]}")