def compare(array1,array2):
    if len(array1)==len(array2):
        for x in range(len(array1)):
            y=0
            while y<=5:
                if array1[x] != array2[x]:
                    return False
                else:
                    y+=1
            
        return True
    else:
        return False

print(compare(["water","book","sky"],["water","book","sky"]))