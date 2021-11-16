array1 = [4,36,12,28,9,44,5]
array2 = [5,1,36]

def unique(numbers1,numbers2):
    new = []
    for x in range(len(numbers1)):
        w=0
        while w<=len(numbers2):
            if numbers1[x]==numbers2[w]:
                break
            if numbers1[x]!=numbers2[w]:
                w+=1
            if w==len(numbers2):
                new.append(numbers1[x])
                break
    return new
            
print(unique(array1,array2))
            
            
            
           