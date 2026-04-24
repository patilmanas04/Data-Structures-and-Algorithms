def checkPrime(n: int) -> bool:
  isPrime = True
  for i in range(2, int(n/2)):
    if n%i==0:
      isPrime=False
      break
  return isPrime

n = int(input("Enter a number: "))
print(checkPrime(n))