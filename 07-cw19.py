file1 = open("MeatAndFish.txt","r")
file2 = open("GrainsAndBread.txt","r")
with open("shoppinglist.txt","w") as shoppinglist:
    shoppinglist.write(file1.read())
    shoppinglist.write(file2.read())
    
file1.close()
file2.close()