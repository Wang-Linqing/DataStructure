class BinaryTree:
    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class Solution:
    @staticmethod
    def is_mirror_tree(root):
        if root is None:
            return True
        return Solution.traversal(root.left,root.right)
    @staticmethod
    def traversal(rootA,rootB):
        if rootA is None and rootB is None:
            return True
        if rootA is not  None and rootB is not  None:
            if rootB.data==rootA.data:
                return Solution.traversal(rootA.left,rootB.right) and Solution.traversal(rootA.right,rootB.left)
            else:
                return False
        else:
            return False