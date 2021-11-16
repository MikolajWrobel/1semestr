from mymath import read_number,generate_number
x = read_number()
y = generate_number()
if x==y:
    print(f"Entered number {x}\nGenerated number: {y}")
    print("You won")
else:
    print(f"Entered number {x}\nGenerated number: {y}")   
    print("You lost")

