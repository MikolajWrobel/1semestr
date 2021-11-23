import re
with open("grades.txt","r") as file:
    file_read = file.read()
    grades = re.findall("\d\.\d",file_read)
    x=0
    for grade in grades:
        x=x+float(grade)
    average = x/len(grades)
print(f"Arithmetic mean of student's grades: {round(average,2)}")