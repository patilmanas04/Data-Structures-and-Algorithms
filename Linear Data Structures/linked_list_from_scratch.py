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
    if self.isEmpty():
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
  
  def recursiveTraverse(self, head):
    if head==None:
      print(None)
      return
    print(head.data, end=" -> ")
    self.recursiveTraverse(head.next)
  
  def recursiveReversePrint(self, head):
    if head==None:
      return
    self.recursiveReversePrint(head.next)
    print(head.data, end=" -> ")

  def recursiveReverse(self, head):
    if head==None or head.next==None:
      self.head=head
      return head
    nextHead=self.recursiveReverse(head.next)
    nextHead.next=head
    head.next=None
    return head

  def sum(self):
    totalSum=0
    current=self.head
    while current:
      totalSum+=current.data
      current=current.next
    return totalSum
  
  def insertAtBeginning(self, data):
    node=Node(data)
    if self.isEmpty():
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
  
  def removeStart(self):
    if self.isEmpty():
      raise ValueError("cannot remove the leftmost element from an empty list")
    temp=self.head
    self.head=self.head.next
    if self.isEmpty():
      self.tail=None
    temp.next=None

  def remove(self):
    if self.isEmpty():
      raise ValueError("cannot remove the rightmost element from an empty list")
    if len(self)==1:
      self.removeStart()
      return
    newTail=self.nodeAtIndex(len(self)-2)
    newTail.next=None
    self.tail=newTail
  
  def __len__(self):
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

# myLinkedList.traverse()
# print(f"Length of linked list: {len(myLinkedList)}")

# myLinkedList.insertAt(2, 99)
# myLinkedList.traverse()
# print(f"Length of linked list: {len(myLinkedList)}")

# myLinkedList.insertAt(0, 0)
# myLinkedList.traverse()
# print(f"Length of linked list: {len(myLinkedList)}")

# # myLinkedList.insertAt(-1, 0)
# myLinkedList.insertAt(11, 100)
# myLinkedList.traverse()
# print(f"Length of linked list: {len(myLinkedList)}")

# # myLinkedList.insertAt(13, 100)

# myLinkedList.removeStart()
# myLinkedList.traverse()
# print(f"Length of linked list: {len(myLinkedList)}")

# myLinkedList2=SinglyLinkedList()
# myLinkedList2.insert(1)
# myLinkedList2.traverse()
# myLinkedList2.removeStart()
# myLinkedList2.traverse()
# print(myLinkedList2.head)
# print(myLinkedList2.tail)
# myLinkedList2.removeStart() # Throws an error as the list is empty

# myLinkedList3=SinglyLinkedList()
# for i in range(3):
#   myLinkedList3.insert(i+1)
# myLinkedList3.traverse()
# print(myLinkedList3.tail.data)

# myLinkedList3.remove()
# myLinkedList3.traverse()
# print(myLinkedList3.tail.data)

# myLinkedList3.remove()
# myLinkedList3.traverse()
# print(myLinkedList3.tail.data)

# myLinkedList3.remove()
# myLinkedList3.traverse()
# print(myLinkedList3.tail)

# Throws an error
# myLinkedList3.remove()
# myLinkedList3.traverse()
# print(myLinkedList3.tail)

myLinkedList4=SinglyLinkedList()
for i in range(10):
  myLinkedList4.insert(i+1)
myLinkedList4.traverse()
myLinkedList4.recursiveTraverse(myLinkedList4.head)
myLinkedList4.recursiveReversePrint(myLinkedList4.head)

myLinkedList4.recursiveReverse(myLinkedList4.head)
print()
myLinkedList4.traverse()