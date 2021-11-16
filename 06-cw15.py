colors = ["blue","red","yellow","white","black"]
textfile = open("textfile.txt","w")
for element in colors:
    textfile.write(element+"\n")
textfile.close()