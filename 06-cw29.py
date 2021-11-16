array1 = [1,2,3]
array2 = [1,2,3,4,5]
array3 = [3,4,5]
array4 = [1,2,3]
def subset(array1,array2):
    for x in array1:
        w=0
        while w<len(array2):
            if x==array2[w]:
                break
            if x!=array2[w]:
                w+=1
            if w==len(array2):
                return f"{array1} is not a subset of {array2}"
    return f"{array1} is a subset of {array2}"

print(subset(array1,array2))
print(subset(array3,array4))