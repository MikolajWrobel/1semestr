import re
with open("07-cw27.txt","r") as file:
    file_read = file.read()
    words = re.findall("\w{6,100}",file_read)
    for x in words:
        print(x)
