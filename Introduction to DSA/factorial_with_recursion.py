def findFactorial(n: int) -> int:
  if n==0:
    return 1
  elif n==1:
    return 1
  else:
    return n * findFactorial(n-1)

n = int(input("Enter a number: "))
print(findFactorial(n))