# O(1)
arr = [1, 2, 3, 4, 5]
print(arr[0])  # No matter what the size of the input is, it will always take constant time to print the first element of the array

new_arr = arr

new_arr[0]+=1 # TC = O(1), SC = O(1)
last_index = len(arr)-1 # TC = O(1), space = 4 bytes (int) => SC = O(4)

print(new_arr[0]) # TC = O(1), SC = O(1)

# TC = O(1) + O(1) + O(1) = O(3) = O(1) => Constant Time Complexity
# SC = O(1) + O(4) + O(1) = O(6) = O(1) => Constant Space Complexity