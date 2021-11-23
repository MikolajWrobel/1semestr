with open("07-cw22.txt","w") as file:
    for x in range(1,11):
        file.write(f"{x},{x**2},{x**3}\n")