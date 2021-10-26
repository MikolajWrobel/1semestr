x=int(input("Enter x coordinate: "))
y=int(input("Enter y coordinate: "))
if x==0 and y==0:
    print(f"Point ({x},{y}) is at the origin of the coordinate system")
elif x==0:
    print(f"Point ({x},{y}) is on the y axis of the coordinate system")
elif y==0:
    print(f"Point ({x},{y}) is on the x axis of the coordinate system")
elif x>0 and y>0:
    print(f"Point ({x},{y}) is in the first quadrant of the coordinate system")
elif x<0 and y>0:
    print(f"Point ({x},{y}) is in the second quadrant of the coordinate system")
elif x<0 and y<0:
    print(f"Point ({x},{y}) is in the third quadrant of the coordinate system")
else:
    print(f"Point ({x},{y}) is in the fourth quadrant of the coordinate system")