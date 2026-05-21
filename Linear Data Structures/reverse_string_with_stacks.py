from stack_from_scratch import Stack

print()
STRING_INPUT=input("Enter a string: ")

stack=Stack(len(STRING_INPUT))

for char in STRING_INPUT:
  stack.push(char)

print(stack)

for i in range(len(STRING_INPUT)):
  print(stack.pop(), end="")