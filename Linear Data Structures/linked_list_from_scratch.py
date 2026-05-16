# import time

class Node:
  def __init__(self, data):
    self.data=data
    self.next=None

# node1=Node(1)
# node2=Node(2)
# node3=Node(3)
# node4=Node(4)
# node5=Node(5)

# node1.next=node2
# node2.next=node3
# node3.next=node4
# node4.next=node5

# head=node1
# current=head
# while current:
#   print(current.data, end=" -> ")
#   current=current.next
# print("Null")

class SinglyLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None

  def insert(self, data):
    node = Node(data)
    if self.head==None:
      self.head=node
      self.tail=node
    else:
      self.tail.next=node
      self.tail=node

  def insertAt(self, index, data):
    if index<0:
      raise IndexError("Invalid Index")
    elif index==0:
      self.insertAtBeginning(data)
      return
    elif index>=len(self):
      raise IndexError("Index out of range")
    node=Node(data)
    prevNode=self.nodeAtIndex(index-1)
    node.next=prevNode.next
    prevNode.next=node
    
  def nodeAtIndex(self, index):
    initialIndex=0
    current=self.head
    while initialIndex<index:
      current=current.next
      initialIndex+=1
    return current

  def traverse(self):
    current=self.head
    while current:
      print(current.data, end=" -> ")
      current=current.next
    print(None)

  def sum(self):
    totalSum=0
    current=self.head
    while current:
      totalSum+=current.data
      current=current.next
    return totalSum
  
  def insertAtBeginning(self, data):
    node=Node(data)
    if self.head==None:
      self.head=node
      self.tail=node
    node.next=self.head
    self.head=node

  def indexOf(self, data):
    index=0
    current=self.head
    while current:
      if current.data==data:
        return index
      current=current.next
      index+=1
    return -1
  
  def __len__(self):
    length=0
    if self.head==None:
      return length
    current=self.head
    while current:
      length+=1
      current=current.next
    return length

myLinkedList=SinglyLinkedList()
# myLinkedList.insert(1)
# myLinkedList.insert(2)

for i in range(10):
  myLinkedList.insert(i+1)

# start=time.time()
# myLinkedList.traverse()
# end=time.time()
# print(f"Time taken: {end-start:.2f}")

# print(f"Total sum: {myLinkedList.sum()}")

# myLinkedList.insertAtBeginning(0)
# myLinkedList.insertAtBeginning(-2)
# myLinkedList.insertAtBeginning(-3)

# myLinkedList.traverse()

# print(myLinkedList.indexOf(10))
# print(myLinkedList.indexOf(2))
# print(myLinkedList.indexOf(5))
# print(myLinkedList.indexOf(100))

myLinkedList.traverse()
print(f"Length of linked list: {len(myLinkedList)}")

myLinkedList.insertAt(2, 99)
myLinkedList.traverse()
print(f"Length of linked list: {len(myLinkedList)}")

myLinkedList.insertAt(0, 0)
myLinkedList.traverse()
print(f"Length of linked list: {len(myLinkedList)}")

# myLinkedList.insertAt(-1, 0)
myLinkedList.insertAt(11, 100)
myLinkedList.traverse()
print(f"Length of linked list: {len(myLinkedList)}")

# myLinkedList.insertAt(13, 100)