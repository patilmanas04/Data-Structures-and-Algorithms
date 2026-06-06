class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.leftChild = left
        self.rightChild = right

    def __str__(self) -> str:
        return str(self.val)

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def recInsert(self, root, val):
        if root==None:
            root=TreeNode(val)
            return root
        if val<root.val:
            root.leftChild=self.recInsert(root.leftChild, val)
        else:
            root.rightChild=self.recInsert(root.rightChild, val)
        return root

    def insert(self, val):
        self.root=self.recInsert(self.root, val)
    
    def preOrderTraversal(self, root):
        values = []
        def helper(node):
            if node==None:
                return
            # Pre-order traversal: Root -> Left -> Right
            values.append(node.val) # Root
            helper(node.leftChild) # Left
            helper(node.rightChild) # Right
        helper(root)
        return values
    
    def inOrderTraversal(self, root):
        values=[]
        def helper(node):
            if node==None:
                return
            # In-order traversal: Left -> Root -> Right
            helper(node.leftChild) # Left
            values.append(node.val)
            helper(node.rightChild)
        helper(root)
        return values
    
    def postOrderTraversal(self, root):
        values=[]
        def helper(node):
            if node==None:
                return
            # Post-order traversal: Left -> Right -> Root
            helper(node.leftChild)
            helper(node.rightChild)
            values.append(node.val)
        helper(root)
        return values

    def traverse(self, method="pre"):
        match method:
            case "pre":
                return self.preOrderTraversal(self.root)
            case "in":
                return self.inOrderTraversal(self.root)
            case "post":
                return self.postOrderTraversal(self.root)
            case "lvl":
                return self.levelOrderTraversal(self.root)
            case _:
                raise ValueError("unknown traversal method")
            
    def heightOfTree(self, root):
        if root==None:
            return -1
        height=max(self.heightOfTree(root.leftChild), self.heightOfTree(root.rightChild))+1
        return height
    
    def getHeightOfTree(self):
        return self.heightOfTree(self.root)
    
    def getHeightOfNode(self, value):
        def helper(node, value):
            if node==None:
                return None
            if node.val==value:
                return self.heightOfTree(node)
            if value<node.val:
                return helper(node.leftChild, value)
            return helper(node.rightChild, value)
        return helper(self.root, value)
    
    def getDepth(self, value):
        def helper(node, value, depth):
            if node==None:
                return None
            if node.val==value:
                return depth
            if value<node.val:
                return helper(node.leftChild, value, depth+1)
            return helper(node.rightChild, value, depth+1)
        return helper(self.root, value, 0)

    def getMinNode(self):
        def helper(node):
            if node==None:
                return None
            if node.leftChild==None:
                return node
            return helper(node.leftChild)
        return helper(self.root)

    def recfind(self, root, val):
        if root==None:
            return None
        if val==root.val:
            return root
        if val<=root.val:
            return self.recfind(root.leftChild, val)
        else:
            return self.recfind(root.rightChild, val)
        
    def isEquals(self, tree):
        def helper(node1, node2):
            if node1==None and node2==None:
                return True
            if node1==None:
                return False
            if node2==None:
                return False
            return node1.val==node2.val and helper(node1.leftChild, node2.leftChild) and helper(node1.rightChild, node2.rightChild)
        return helper(self.root, tree.root)
    
    def nodesAtDistance(self, k):
        values=[]
        def distance(node, k):
            if not node:
                return
            if k==0:
                values.append(node.val)
            distance(node.leftChild, k-1)
            distance(node.rightChild, k-1)
        distance(self.root, k)
        return values or None

    def find(self, val):
        return self.recfind(self.root, val)

    def isEmpty(self):
        return self.root == None

binarySearchTree = BinarySearchTree()
# nums = [7, 8, 1, 3, 2, 5, 10, 4]
nums = [7, 3, 8, 1, 4, 7, 10, 1, 2, 10, 11, 12, -1]
for i in nums:
    binarySearchTree.insert(i)

for i in range(binarySearchTree.getHeightOfTree()+1):
    print(f"Nodes at level: {binarySearchTree.nodesAtDistance(i)}")