def countPrimes(n: int) -> int:
  primeMatrix = [False, False] + [True] * (n-2)
  primeCount = 0
  for index, value in enumerate(primeMatrix):
    if value:
      primeCount+=1
      for i in range(index*2, len(primeMatrix), index):
        primeMatrix[i] = False
  return primeCount

n = int(input("Enter the value of n: "))
print(countPrimes(n))