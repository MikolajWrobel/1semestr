def star(n):
    return f"{n}: {'*'*n}"

numbers = [12,6,4,9,3]

for x in range(len(numbers)):
    print(star(numbers[x]))