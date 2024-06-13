# O(n^2)

arr = [3, 4, 5, 10, 0, 5, 6, 25, 30]
target_sum = 9

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j]==target_sum:
            print(f"Pair: ({arr[i]}, {arr[j]})")