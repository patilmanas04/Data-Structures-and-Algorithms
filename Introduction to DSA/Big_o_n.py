# O(n)
arr = [1, 2, 3, 4, 5] 

arr[0] += 10

for i in arr: # TC = O(n) | SC = O(1)
  print(i)

print(arr[len(arr)-1]) # TC = O(1) | SC = O(1)

new_arr = [] # TC = O(1) | # SC = O(1)

for i in arr: # TC = O(n) | SC = O(n)
  new_arr.append(i)

for i in new_arr: # TC = O(n) | SC = O(1)
  print(i)

print(arr[len(arr)-1]) # TC = O(1) | # SC = O(1)

# TC = n + 1 + 1 + n + n + 1 = O(3n + 3) = O(n)
# SC = 1 + 1 + 1 + n + 1 + 1 = O(5 + n) = O(n)