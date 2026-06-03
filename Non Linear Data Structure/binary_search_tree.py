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
        if val<=root.val:
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
    
    def recfind(self, root, val):
        if root==None:
            return None
        if val==root.val:
            return root
        if val<=root.val:
            return self.recfind(root.leftChild, val)
        else:
            return self.recfind(root.rightChild, val)

    def find(self, val):
        return self.recfind(self.root, val)

    def isEmpty(self):
        return self.root == None

binarySearchTree = BinarySearchTree()
nums = [7, 8, 1, 3, 2, 5, 10, 4]
for i in nums:
    binarySearchTree.insert(i)

print(binarySearchTree.find(10))
print(binarySearchTree.find(4))
print(binarySearchTree.find(20))
print(binarySearchTree.find(11))