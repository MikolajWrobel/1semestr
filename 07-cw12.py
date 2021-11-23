f = open("shopping.txt","a")
x = str(input("Enter a product: "))
f.write(f"{x}\n")
f.close

f = open("shopping.txt","r")
f.close