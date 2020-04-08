import unittest

class BinaryTree:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class Solution:
    def get_the_depth_of_binary_tree(self,root):
        if root is None:
            return 0
        return self.traverse(root)
    def traverse(self,root):
        left_depth=1
        right_depth=1
        if root.left is not None:
            left_depth+=self.traverse(root.left)
        if root.right is not None:
            right_depth+=self.traverse(root.right)
        return max(right_depth,left_depth)
    def is_balanced_traverse(self,root):
        left_depth=0
        right_depth=0
        is_b_l=True
        is_b_r=True

        if root.left is not None:
            is_b_l,left_depth=self.is_balanced_traverse(root.left)
        if root.right is not None:
            is_b_r,right_depth=self.is_balanced_traverse(root.right)
        is_balanced=True
        if abs(right_depth-left_depth)<=1:
            is_balanced=True
        else:
            is_balanced=False
        is_balanced=is_balanced and is_b_l and is_b_r
        return is_balanced,max(right_depth+1,left_depth+1)


    def is_balanced_binary_tree(self,root):
        if root is None:
            return True
        is_b,depth=self.is_balanced_traverse(root)
        return is_b


class Test(unittest.TestCase):
    obj=Solution()
    def test_1(self):
        b1=BinaryTree(1)
        b2=BinaryTree(1)
        b3=BinaryTree(1)
        b4=BinaryTree(1)
        b5=BinaryTree(1)
        b6=BinaryTree(1)
        b7=BinaryTree(1)
        b1.left=b2
        b1.right=b3
        b2.left=b4
        b2.right=b5
        b5.left=b7
        b3.right=b6
        self.assertEqual(self.obj.get_the_depth_of_binary_tree(b1), 4)

    def test_2(self):
        b1=BinaryTree(1)
        b2=BinaryTree(1)
        b3=BinaryTree(1)
        b4=BinaryTree(1)
        b5=BinaryTree(1)
        b6=BinaryTree(1)
        b7=BinaryTree(1)
        b1.left=b2
        b1.right=b3
        b2.left=b4
        b2.right=b5
        b5.left=b7
        b3.right=b6
        b8=BinaryTree(8)
        b7.right=b8
        self.assertEqual(self.obj.is_balanced_binary_tree(b1), False)

    def test_3(self):
        self.assertEqual("", "")

    def test_4(self):
        self.assertEqual("", "")

    def test_5(self):
        self.assertEqual("", "")

    def test_6(self):
        self.assertEqual("", "")

    def test_7(self):
        self.assertEqual("", "")

    def test_8(self):
        self.assertEqual("", "")
