# n = int(input("Enter a decimal number: "))
# decimal = n
# binary = ""
# while n!=0:
#   binary = str(n&1) + binary
#   n = n>>1
# print(f"(Decimal) {decimal} = (Binary) {binary}")

n = -123
reversed = 0
while n!=0:
    last_digit = n%10
    print(f"Last digit: {last_digit}")
    reversed = 10*reversed + last_digit
    print(f"Reversed: {reversed}")
    n = int(n/10)

print(f"Final Output: {reversed}")