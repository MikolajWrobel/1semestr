for x in range(1,31):
    if x%3>0 and x%5>0:
        print(x)
    elif x%3==0 and x%5==0:
        print("Bingo!")
    elif x%3==0:
        print("Three")
    elif x%5==0:
        print("Five")
    
    