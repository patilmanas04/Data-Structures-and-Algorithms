class MaxHeap:
  def __init__(self, size):
    self.size=size
    self.heap=[0]*size
    self.index=0

  def insert(self, val):
    if not self.index<self.size:
      raise IndexError("Cannot insert as the head is already full")
  
    self.heap[self.index]=val
    self.index+=1

    # Check for max heap property and bubble up
    current_index=self.index-1
    while current_index>0 and self.heap[current_index]>self.getParentVal(current_index):
      self.swapValues(current_index, self.getParentIndex(current_index))
      current_index=self.getParentIndex(current_index)

  def getParentIndex(self, current_index):
    return (current_index-1)//2
  
  def getParentVal(self, current_index):
    return self.heap[self.getParentIndex(current_index)]
  
  def swapValues(self, index1, index2):
    temp=self.heap[index1]
    self.heap[index1]=self.heap[index2]
    self.heap[index2]=temp

values=[3, 10, 5, 8, 16, 20, 90]
max_heap=MaxHeap(len(values))

for n in values:
  max_heap.insert(n)

pass