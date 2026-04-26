import array

class IntArray:
  def __init__(self, initialSize: int) -> None:
    self.__array = array.array("i", [0]*initialSize)
    self.__currentIndex = 0;

  def insert(self, value: int) -> None:
    self.__array[self.__currentIndex] = value
    self.__currentIndex += 1

  def indexOf(self, value: int) -> int:
    for i in range(self.__currentIndex):
      if self.__array[i] == value:
        return i
    return -1
  
  def removeAt(self, index: int):
    if index<0:
      raise ValueError("array index cannot be a negative value.")
    if index>=self.__currentIndex:
      raise IndexError(f"the index {index} is out of range for the array.")
    for i in range(index, self.__currentIndex-1):
      self.__array[i] = self.__array[i+1]
    self.__array[self.__currentIndex-1]=0
    self.__currentIndex-=1

  def max(self) -> int:
    maxValue = self.__array[0]
    for index in range(1, self.__currentIndex):
      if self.__array[index]>maxValue:
        maxValue=self.__array[index]
    return maxValue
  
  def min(self) -> int:
    minValue = self.__array[0]
    for index in range(1, self.__currentIndex):
      if self.__array[index]<minValue:
        minValue = self.__array[index]
    return minValue
  
  def reverse(self) -> None:
    for index in range(int(self.__currentIndex/2)+1):
      temp = self.__array[index]
      self.__array[index]=self.__array[self.__currentIndex-index-1]
      self.__array[self.__currentIndex-index-1] = temp

  def dynamicInsert(self, value: int) -> None:
    if self.__currentIndex>=len(self):
      self.__newArray = array.array("i", [0]*(len(self)+5))
      for index in range(self.__currentIndex):
        self.__newArray[index] = self.__array[index]
      self.__array = self.__newArray
      self.__array[self.__currentIndex] = value
      self.__currentIndex += 1

  def __len__(self):
    return self.__currentIndex
  
  def __str__(self):
    startArr = "["
    endArr = "]"
    for i in range(self.__currentIndex):
      startArr = startArr + str(self.__array[i]) + (", " if i!=self.__currentIndex-1 else "")
    startArr += endArr
    return startArr
  
# myarray = IntArray(5)
# myarray.insert(10)
# myarray.insert(30)
# myarray.insert(20)
# print(myarray)

# myarray.removeAt(0)
# print(myarray)
# myarray.removeAt(1)
# print(myarray)
# myarray.insert(50)
# print(myarray)
# myarray.insert(60)
# print(myarray)
# myarray.insert(40)
# print(myarray)
# print(myarray.max())
# print(myarray.min())
# myarray.insert(-10)
# print(myarray.min())
# print(len(myarray))

evenArray = IntArray(6)
oddArray = IntArray(5)

for i in range(6):
  evenArray.insert(i+1)
print(f"Even Array: {evenArray}")

for i in range(5):
  oddArray.insert(i+1)
print(f"Odd Array: {oddArray}")

evenArray.reverse()
print(f"Reversed even array: {evenArray}")

oddArray.reverse()
print(f"Reversed Odd Array: {oddArray}")

evenArray.reverse()
print(evenArray)
# evenArray.insert(7) # This will result in an error
evenArray.dynamicInsert(7)
print(evenArray)
print(len(evenArray))