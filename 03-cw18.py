x=int(input("Enter an amout of PLN: "))
print(f"The amount of PLN {x} in coins:")
n5=(x // 5)
n2=(x-(n5 * 5)) // 2
n1=(x-(n5 * 5)-(n2 * 2))
print(f"5zł - ",int(n5))
print(f"2zł - ",int(n2))
print(f"1zł - ",int(n1))

