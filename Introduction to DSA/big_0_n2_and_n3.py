arr = [3, 4, 5, 10, 0, 5, 6, 25, 30]

target = 10
# Find the pairs whose sum is equal to 10
for i in range(len(arr)):
  for j in range(i+1, len(arr)):
    if arr[i]+arr[j]==target:
      print(f"Pair: ({arr[i]}, {arr[j]})")