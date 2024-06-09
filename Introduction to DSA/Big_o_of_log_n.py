import time

# O(log n)

arr = list(range(1, 101)) # TC - O(1) SP - O(1)

# We want to search element 8 in the array
# Using Linear Search
start_time = time.time() 
for i in arr: # TC - O(n) SP - O(1)
    if i == 80:
        print("[Linear Search] Element found at index: ", arr.index(i))
        break

end_time = time.time()
execution_time = end_time * 1000 - start_time * 1000
print("Time taken by Linear Search: ", execution_time, " seconds")

# Using Binary Search
# Binary Search is a divide and conquer algorithm
start_time = time.time()
start = 0 
end = len(arr) - 1 
element_to_search = 80
while start <= end: # TC - O(log n) SP - O(1)
    mid = (start + end) // 2
    if arr[mid] == element_to_search:
        print("[Binary Search] Element found at index: ", mid);
        break;
    elif arr[mid] < element_to_search:
        start = mid + 1
    else:
        end = mid - 1

end_time = time.time()
execution_time = end_time * 1000 - start_time * 1000
print("Time taken by Binary Search: ", execution_time, " seconds")