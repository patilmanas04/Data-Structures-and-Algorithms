import array
arr = array.array('i', [0]*5)

arr[0] = 1
arr[1] = 2
arr[2] = 3
arr[3] = 4
arr[4] = 5
# arr[4] = "Manas" # Will cause an error

print(arr)
print(arr[3])