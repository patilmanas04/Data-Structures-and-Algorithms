# O(1) - Constant Time

arr = [1, 2, 3, 4, 5, 6]; # TC - O(1) SP - O(1)
# Input size of the array doesn't matter

arr[0] = arr[0] + 10; # TC - O(1) SP - O(1)
num = arr[len(arr) - 1]; # TC - O(1) SP - O(1)

print(arr[0]); # TC - O(1) SP - O(1)

# Total TC and SP
# TC - O(1) + O(1) + O(1) = O(3) = O(1) - Constant Time
# SP - O(1) + O(1) + O(1) = O(3) = O(1) - Constant Space

# The time complexity of an algorithm is said to be constant time if the execution time is the same for all inputs.