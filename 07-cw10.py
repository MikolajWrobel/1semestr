f = open("name.txt","w")
f.write("Mikołaj Wróbel\nUEK w Krakowie\nInformatyka stosowana")
f.close

f = open("name.txt","r")
print(f.read())