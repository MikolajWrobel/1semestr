numbers = [2,3,2,5,8,1,9,8]

z=''
for x in range(len(numbers)):
    w=0
    while w<(len(numbers)):
        if w==x:
            w+=1
        elif numbers[x]==numbers[w]:
            break
        elif numbers[x]!=numbers[w]:
            w+=1
    if w==len(numbers):
        z=f"{z} {numbers[x]}"

y=''
for x in range(len(numbers)):
    y=f"{y} {numbers[x]}"
    
print(f"Array:{y}")
print(f"Unique elements:{z}")
                


    
    

            