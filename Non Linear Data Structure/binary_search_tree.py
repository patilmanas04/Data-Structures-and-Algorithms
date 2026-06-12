from collections import deque

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
        # 1. Inserting values in a BST using loops
        # if self.isEmpty():
        #     self.root = TreeNode(val)
        #     return
        # current = self.root
        # while True:
        #     if val <= current.val:
        #         if not current.leftChild:
        #             current.leftChild=TreeNode(val)
        #             return
        #         current=current.leftChild
        #     else:
        #         if not current.rightChild:
        #             current.rightChild=TreeNode(val)
        #             return
        #         current=current.rightChild

        # 2. Inserting values in BST using Recursion (Mostly Recursion is used while dealing with Trees)
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
    
    def levelOrderTraversal(self, node):
        queue=deque()
        queue.append(node)
        values=[]
        while queue:
            temp=[]
            for i in range(len(queue)):
                tempNode=queue.popleft()
                temp.append(tempNode.val)
                if tempNode.leftChild:
                    queue.append(tempNode.leftChild)
                if tempNode.rightChild:
                    queue.append(tempNode.rightChild)
            values.append(temp)
        return values
    
    def morrisInOrderTraversal(self, root):
        current=root
        values=[]
        while current:
            if not current.leftChild:
                values.append(current.val)
                current=current.rightChild
            else:
                pred=current.leftChild
                while pred.rightChild and pred.rightChild!=current:
                    pred=pred.rightChild
                if not pred.rightChild:
                    pred.rightChild=current
                    current=current.leftChild
                else:
                    pred.rightChild=None
                    values.append(current.val)
                    current=current.rightChild
        return values
    
    def morrisPreOrderTraversal(self, root):
        current=root
        values=[]
        while current:
            if not current.leftChild:
                values.append(current.val)
                current=current.rightChild
            else:
                pred=current.leftChild
                while pred.rightChild and pred.rightChild!=current:
                    pred=pred.rightChild
                if not pred.rightChild:
                    values.append(current.val)
                    pred.rightChild=current
                    current=current.leftChild
                else:
                    pred.rightChild=None
                    current=current.rightChild
        return values

    def traverse(self, method="pre"):
        match method:
            case "pre":
                return self.preOrderTraversal(self.root)
            case "mpre":
                # Morris Pre-order traversal
                return self.morrisPreOrderTraversal(self.root)
            case "in":
                return self.inOrderTraversal(self.root)
            case "min":
                # Morris In-order traversal
                return self.morrisInOrderTraversal(self.root)
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

    def find(self, val):
        return self.recfind(self.root, val)

    def isEmpty(self):
        return self.root == None

binarySearchTree = BinarySearchTree()
nums = [7, 8, 1, 3, 2, 5, 10, 4]
for i in nums:
    binarySearchTree.insert(i)
print(f"Level-order traversal: {binarySearchTree.traverse(method="lvl")}")
print()

# print(binarySearchTree.find(10))
# print(binarySearchTree.find(4))
# print(binarySearchTree.find(20))
# print(binarySearchTree.find(11))

newBST=BinarySearchTree()
newBST1=BinarySearchTree()
treeValues=[7, 3, 8, 1, 4, 7, 10, 1, 2, 10, 11, 12, -1]
treeValues1=[7, 3, 8, 1, 4, 7, 10, 1, 2, 10, 11, 12]
for i in treeValues:
    newBST.insert(i)
for i in treeValues1:
    newBST1.insert(i)

print(f"Pre-order traversal: {newBST.traverse(method="pre")}")
print(f"Morris Pre-order traversal: {newBST.traverse("mpre")}")
print(f"In-order traversal: {newBST.traverse(method="in")}")
print(f"Morris In-order traversal: {newBST.traverse("min")}")
print(f"post-order traversal: {newBST.traverse(method="post")}")
print(f"Level-order traversal: {newBST.traverse(method="lvl")}")
# print(f"In-order traversal: {newBST.traverse(method="mkc")}") # This will throw an error
print()
print(f"Height of the tree: {newBST.getHeightOfTree()}")
print(f"Height of the node 7: {newBST.getHeightOfNode(7)}")
print(f"Height of the node 8: {newBST.getHeightOfNode(8)}")
print(f"Height of the node 11: {newBST.getHeightOfNode(11)}")
print(f"Height of the node 12: {newBST.getHeightOfNode(12)}")
print()
print(f"Depth of the node 7: {newBST.getDepth(7)}")
print(f"Depth of the node 8: {newBST.getDepth(8)}")
print(f"Depth of the node 11: {newBST.getDepth(11)}")
print(f"Depth of the node 12: {newBST.getDepth(12)}")
print()
print(f"Min value in the tree: {newBST.getMinNode()}")
print()
print(f"Equals: {newBST.isEquals(newBST1)}")