numbers = [15,8,31,47,2,19]
y=''
for x in range(len(numbers)):
    y = f"{y} {numbers[x]}"
z=''
for x in range(len(numbers)):
    z = f"{z} {numbers[len(numbers)-1-x]}"

print(f"existed array:{y}")
print(f"reverse array:{z}")