film_titles = ["Star wars","Interstellar","The Martian",
               "Inception","First man"]

f = open("film_titles.txt","w")
for x in range(len(film_titles)):
    f.write(f"{film_titles[x]}\n")
    
f = open("film_titles.txt","r")
print(f.read())
