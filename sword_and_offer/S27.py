class BinaryTree:
    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class Solution:
    @staticmethod
    def traversal_to_mirror(root):
        if root is None:
            return None
        tmp=root.left
        root.left=root.right
        root.right=tmp
        if root.left is not None:
            Solution.traversal_to_mirror(root.left)
        if root.right is not None:
            Solution.traversal_to_mirror(root.right)
        return root
