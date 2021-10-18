heightincm=185

feet=heightincm*0.032808399
feet1=int(feet)
inches=(heightincm*0.032808399-feet1)*12
inches1=int(inches)
print("I am",heightincm,"cm tall, i.e.",feet1,"feet and",inches1,"inches")
