class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(7)
root.left = TreeNode(1)
root.right = TreeNode(8)
root.left.right = TreeNode(3)
root.right.right = TreeNode(10)
