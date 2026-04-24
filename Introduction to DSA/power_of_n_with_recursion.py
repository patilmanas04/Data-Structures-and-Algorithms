def power(x: int, n: int) -> int:
  if n==0:
    return 1
  if n==1:
    return x
  else:
    return x*power(x, n-1)
  
x = int(input("x: "))
n = int(input("n: "))
print(power(x, n))