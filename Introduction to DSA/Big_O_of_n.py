# O(n) - Linear Time

arr = [1, 2, 3, 4, 5, 6]; # TC - O(1) SP - O(1)
# Time Complexity is directly proportional to the size of the input data

arr[0] = arr[0] + 10; # TC - O(1) SP - O(1)

print("Printing the elements of the array: ");
for element in arr: # TC - O(n) SP - O(1)
    print(element);

arr_copy = [] # TC - O(1) SP - O(n)

for i in arr: # TC - O(n) SP - O(1)
    arr_copy.append(i);

print("\nPrinting the elements of the copied array: ");
for element in arr_copy: # TC - O(n) SP - O(1)
    print(element);

# Total
# TC - O(1) + O(1) + O(n) + O(1) + O(n) + O(1) + O(n) = O(3n + 3) = O(n) - Linear Time
# SP - O(1) + O(1) + O(1) + O(n) + O(1) + O(n) + O(1) = O(3n + 3) = O(n) - Linear Space

# The time complexity of an algorithm is said to be linear time if the execution time is directly proportional to the size of the input data.