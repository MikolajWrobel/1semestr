tab=[15,8,31,47,2,19]
even=0
odd=0
for i in tab:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(f"Even:{even},Odd:{odd}")