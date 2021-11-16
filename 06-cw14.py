names = ["Genowefa","Onufry","Celestyna",
         "Alojzy","Pankracy"]
z = names[0]
for x in range(len(names)):
    if len(names[x])>len(z):
        z = names[x]

y=''
for x in range(len(names)):
    y=f"{y} {names[x]}"

print(f"Names:{y}")
print(f"Longest name: {z}")
