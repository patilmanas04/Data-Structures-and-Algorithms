decimal = int(input("Enter a decimanl number to convert it to binary: "))
dec_copy = decimal
remainders = []
while decimal!=0:
  remainders.append(decimal%2)
  decimal = decimal // 2

print(f"Decimanl ({dec_copy}): Binary({int("".join(map(str, remainders[::-1])))})")