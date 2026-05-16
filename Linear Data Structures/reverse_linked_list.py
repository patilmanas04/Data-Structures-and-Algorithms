class Node:
  def __init__(self, data):
    self.data=data
    self.next=None

class SinglyLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None

  def insert(self, data: any) -> None:
    node = Node(data)
    if self.isEmpty():
      self.head=node
      self.tail=node
    else:
      self.tail.next=node
      self.tail=node

  def traverse(self) -> None:
    current=self.head
    while current:
      print(current.data, end=" -> ")
      current=current.next
    print(None)

  def reverse(self) -> None:
    if self.isEmpty():
      raise ValueError("cannot reverse an empty linked list")
    prev=None
    current=self.head
    next=current.next
    while True:
      current.next=prev
      if next==None:
        break
      prev=current
      current=next
      next=next.next
    temp=self.head
    self.head=self.tail
    self.tail=temp

  def __len__(self) -> int:
    length=0
    if self.isEmpty():
      return length
    current=self.head
    while current:
      length+=1
      current=current.next
    return length
  
  def isEmpty(self):
    return self.head==None
  
linkedList=SinglyLinkedList()
for i in range(10):
  linkedList.insert(i+1)
linkedList.traverse()

linkedList.reverse()
linkedList.traverse()