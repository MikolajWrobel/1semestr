with open("RandomNumbers.txt","w") as file:
    import random
    for x in range(1,51):
        file.write(f"{random.randint(100,999)}\n")