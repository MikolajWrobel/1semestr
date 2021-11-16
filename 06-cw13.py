
numbers = [1,2,3]
z=''
for x in range(len(numbers)):
    z = f"{z} {numbers[x]**2}"

y=''
for x in range(len(numbers)):
    y = f"{y} {numbers[x]}"
    

print(f"Array:{y}")
print(f"second power:{z}")