n = input("Enter a binary number: ")
binary = n
decimal = 0

# Approach 1
for index, value in enumerate(n[::-1]):
  if int(value) == 1:
    decimal += 2**index
print(f"(Binary) {binary} = (Decimal) {decimal}")

# Approach 2
n = int(input("Enter a binary number: "))
decimal=0
index=0
while n!=0:
  last_digit = n%10
  if last_digit==1:
    decimal+=2**index
  n = int(n/10)
  index+=1
print(f"(Binary) {binary} = (Decimal) {decimal}")