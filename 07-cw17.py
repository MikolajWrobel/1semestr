with open("07-cw17.txt","r") as file1:
    with open("copy.txt","w") as file2:
        file2.write(file1.read())