stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print("Elements in the stack:")
for i in range(len(stack), 0, -1):
  print(stack[i-1])

print(stack)
print(f"\nIs stack empty: {True if len(stack)==0 else False}")

print("\nPopping elements one by one:")
print(stack.pop())
print(stack.pop())
print(stack.pop())
# print(stack.pop()) # Throws an error

print()
print(stack)
print(f"Is stack empty: {True if len(stack)==0 else False}")

print()
stack2=[1, 2, 3, 4]
print(stack2)
while len(stack2)!=0:
  print(stack2.pop(), end="\n")