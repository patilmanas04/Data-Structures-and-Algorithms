import time

arr = [2, 5, 7, 10, 20, 35, 40, 60]

searchfor = 40

starttimeforLS = time.perf_counter()
# Linear Search - T.C. is O(n)
for index, value in enumerate(arr):
  if value==searchfor:
    print(f"[LS] Found {searchfor} at {index}")
endtimeforLS = time.perf_counter()

starttimeforBS = time.perf_counter()
# Binary Search - T.C. is O(logn)
start = 0
end = len(arr)-1

for i in range(len(arr)):
  mid = (start+end)//2

  if arr[mid]==searchfor:
    print(f"[BS] Found {searchfor} at {mid}")
    break
  elif searchfor < arr[mid]:
    end = mid-1
  elif searchfor > arr[mid]:
    start = mid+1
endtimeforBS = time.perf_counter()

print(f"Time taken by LS is {endtimeforLS-starttimeforLS} seconds")
print(f"Time taken by BS is {endtimeforBS-starttimeforLS} seconds")