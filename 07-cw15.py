filename = input("Enter file name: ")
with open(filename,"r") as file:
    z=0
    for line in file:
        z+=1
        
print(f"File name: {str(filename)}")
print(f"Number of lines: {z}")