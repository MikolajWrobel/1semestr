def arr2str(array):
    z=f"{array[0]}"
    for x in range(1,len(array)):
        z=f"{z},{array[x]}"
    return f"Array: {array} \nString: {z}"

print(arr2str([5,4,3,2,6,5]))
        