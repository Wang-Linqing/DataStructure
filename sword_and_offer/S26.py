class BinaryTree:
    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class Solution:
    @staticmethod
    def traversal(root,B):
        has_tree=False
        if B is None:
            return True
        if root is None:
            return False
        has_tree=Solution.does_tree_A_has_tree_two(root,B)
        if has_tree:
            return has_tree
        else:
            has_tree=has_tree or Solution.traversal(root.left,B)
        if has_tree:
            return has_tree
        else:
            has_tree=has_tree or Solution.traversal(root.right,B)
            return has_tree


    @staticmethod
    def does_tree_A_has_tree_two(A,B):
        if A.data==B.data:
            if B.left is not None:
                if A.left is None:
                    return False
                else:
                    return Solution.does_tree_A_has_tree_two(A.left,B.left)
            if B.right is not None:
                if A.right is None:
                    return False
                else:
                    return Solution.does_tree_A_has_tree_two(A.right,B.right)
            return True
        else:
            return False
tmp_1=BinaryTree(4)
tmp_2=BinaryTree(7)
tmp_3=BinaryTree(2,tmp_1,tmp_2)
tmp_1=BinaryTree(9)
tmp_2=tmp_3
tmp_3=BinaryTree(8,tmp_1,tmp_2)
B=tmp_3
tmp_1=tmp_3
tmp_2=BinaryTree(7)
tmp_3=BinaryTree(8,tmp_1,tmp_2)
A=tmp_3
C=BinaryTree(2,BinaryTree(4))
print(Solution.traversal(A,C))

