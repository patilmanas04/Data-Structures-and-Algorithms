class StackOverflowException(Exception):
  def __init__(self, message="the stack has reached it's maximum alloted capacity"):
    super().__init__(message)

class EmptyStackException(Exception):
  def __init__(self, message="popping from an empty stack"):
    super().__init__(message)

class Stack:
  def __init__(self, size):
    self.__top=-1
    self.__size=size
    self.stack=[0]*size
  
  def push(self, value):
    if self.__top+1>=self.__size:
      raise StackOverflowException()
    self.__top+=1
    self.stack[self.__top]=value

  def pop(self):
    if self.__top<0:
      raise EmptyStackException
    value=self.stack[self.__top]
    self.stack[self.__top]=0
    self.__top-=1
    return value
  
  def peek(self):
    if self.__top<0:
      raise IndexError("cannot peek from an empty array")
    return self.stack[self.__top]

  def getTop(self):
    return self.__top

  def getSize(self)->int:
    return self.__size

  def __len__(self):
    return self.__top+1

  def __str__(self):
    string="<["
    for i in range(len(self)):
      string+=f"{self.stack[i]}"
      string+=(" " if i!=len(self)-1 else "")
    string+=f"], 'Stack', size={len(self)}>"
    return string
  
  def isEmpty(self):
    return True if self.__top<0 else False
  
stack=Stack(5)
for i in range(5):
  stack.push(i+1)
  print(f"Value: {i+1}")
  print(f"Top: {stack.getTop()}")
print()

# stack.push(6) # Throws an error
print(stack)
print(f"Size of the stack: {stack.getSize()}")
print(f"Is stack empty: {stack.isEmpty()}")
print(f"Peek: {stack.peek()}")
print(f"Top: {stack.getTop()}")
print()

print(f"Top: {stack.getTop()}, Value: {stack.pop()}")
print(f"Top: {stack.getTop()}, Value: {stack.pop()}")
print(f"Top: {stack.getTop()}, Value: {stack.pop()}")
print(f"Top: {stack.getTop()}, Value: {stack.pop()}")
print(f"Top: {stack.getTop()}, Value: {stack.pop()}")
# print(f"Top: {stack.getTop()}, Value: {stack.pop()}") # Throws an error
print(f"Current top: {stack.getTop()}")
print(f"Is stack empty: {stack.isEmpty()}")
# print(stack.peek()) # Throws an error