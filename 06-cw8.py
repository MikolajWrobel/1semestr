numbers = [-15,8,-31,47,-2,19]
min=numbers[0]
max=numbers[0]

for i in numbers:
    if i>max:
        max=i
    if i<min:
        min=i

print(f"Max:{max}, Min:{min}")
