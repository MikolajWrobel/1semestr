array = [1,2,2.5,3,5.5,10]
number = float(input("Enter a real number: "))

z=0
for x in range(len(array)):
    if array[x]>number:
        z+=1

print(f"Array: {array}")
print(f"Entered number: {number}")
print(f"Number of elements that are greater than the\ngiven value entered from the keyboard: {z}")