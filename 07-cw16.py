with open("07-cw16.txt","r") as file:
    z=1
    for line in file:
        print(line,end='')
        z+=1
        if z==6:
            break
        

        