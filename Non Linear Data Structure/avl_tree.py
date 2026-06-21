class AVLNode:
  def __init__(self, val=0, left=None, right=None, height=0):
    self.val=val
    self.left=left
    self.right=right
    self.height=height
  
  def __str__(self):
    return f"Val={self.val}"

class AVLTree:
  def __init__(self):
    self.root=None

  def insert(self, val):
    def addVal(node, val):
      if not node: return AVLNode(val)
      if node.val==val: return node

      if val<node.val:
        node.left=addVal(node.left, val)
      else:
        node.right=addVal(node.right, val)

      node.height=max(self.getHeight(node.left), self.getHeight(node.right))+1
      balanceFactor=self.getBalanceFactor(node)

      if balanceFactor<-1:
        if self.getBalanceFactor(node.right)>0:
          node.right=self.rightRotate(node.right)
        node=self.leftRotate(node)
      if balanceFactor>1:
        if self.getBalanceFactor(node.left)<0:
          node.left=self.leftRotate(node.left)
        node=self.rightRotate(node)

      return node
    self.root=addVal(self.root, val)

  def getHeight(self, node):
    if not node: return -1
    return node.height
  
  def getBalanceFactor(self, node):
    if not node: return 0
    return self.getHeight(node.left)-self.getHeight(node.right)

  def leftRotate(self, node) -> AVLNode:
    newRoot=node.right
    node.right=newRoot.left
    newRoot.left=node
    node.height=max(self.getHeight(node.left), self.getHeight(node.right))+1
    newRoot.height=max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))+1
    return newRoot
  
  def rightRotate(self, node) -> AVLNode:
    newRoot=node.left
    node.left=newRoot.right
    newRoot.right=node
    node.height=max(self.getHeight(node.left), self.getHeight(node.right))+1
    newRoot.height=max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))+1
    return newRoot

avlTree=AVLTree()

# values=[10, 5, 15, 2, 8, 12, 18]
# values=[10, 8, 15, 20, 5, 7]
values=[10, 5, 8, 15, 20, 25]

for val in values:
  avlTree.insert(val)
