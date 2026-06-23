class MaxHeap:
  def __init__(self, size):
    self.size=size
    self.heap=[0]*size
    self.count=0

  def insert(self, val):
    if self.count>=self.size:
      raise IndexError("Cannot insert as the head is already full")
  
    self.heap[self.count]=val
    self.count+=1

    # Check for max heap property and bubble up
    current_index=self.count-1
    while current_index>0 and self.heap[current_index]>self.getParentVal(current_index):
      self.swapValues(current_index, self.getParentIndex(current_index))
      current_index=self.getParentIndex(current_index)

  def remove(self) -> int:
    if self.is_empty():
      raise IndexError("Cannot remove from a empty heap")
    
    elementToRemove=self.heap[0]
    self.count-=1
    self.heap[0]=self.heap[self.count]

    # Check for the max heap property and bubble down
    current_index=0
    while current_index<self.count and not self.is_valid(current_index):
      largest_element_index=self.get_largest_element_index(current_index)
      self.swapValues(current_index, largest_element_index)
      current_index=largest_element_index

    return elementToRemove
  
  def get_largest_element_index(self, current_index):
    if not self.has_right(current_index):
      return self.get_left_index(current_index)
    
    if self.get_left(current_index)>self.get_right(current_index):
      return self.get_left_index(current_index)
    
    return self.get_right_index(current_index)

  def is_valid(self, current_index):
    if not self.has_left(current_index) and not self.has_right(current_index):
      return True

    if not self.has_left(current_index):
      return False
    
    if not self.has_right(current_index):
      return self.heap[current_index] >= self.heap[self.get_left_index(current_index)]
    
    return self.heap[current_index]>=self.heap[self.get_left_index(current_index)] and self.heap[current_index]>=self.heap[self.get_right_index(current_index)]

  def has_left(self, current_index):
    return self.get_left_index(current_index) < self.count
  
  def has_right(self, current_index):
    return self.get_right_index(current_index) < self.count
  
  def get_left_index(self, current_index):
    return current_index*2+1
  
  def get_right_index(self, current_index):
    return current_index*2+2
  
  def get_left(self, current_index):
    return self.heap[self.get_left_index(current_index)]
  
  def get_right(self, current_index):
    return self.heap[self.get_right_index(current_index)]

  def is_empty(self):
    return self.count==0

  def getParentIndex(self, current_index):
    return (current_index-1)//2
  
  def getParentVal(self, current_index):
    return self.heap[self.getParentIndex(current_index)]
  
  def swapValues(self, index1, index2):
    temp=self.heap[index1]
    self.heap[index1]=self.heap[index2]
    self.heap[index2]=temp

values=[3, 10, 5, 8, 16, 20, 90, -1, 100, 999]
max_heap=MaxHeap(len(values))

for n in values:
  max_heap.insert(n)

while not max_heap.is_empty():
  print(max_heap.remove())