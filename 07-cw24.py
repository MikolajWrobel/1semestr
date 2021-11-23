import re
message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"
temperatures = re.findall("\d{2}",message)

x=0
for y in temperatures:
    x = x+int(y)

average = x/len(temperatures)

print(f"Average temperature: {average}")