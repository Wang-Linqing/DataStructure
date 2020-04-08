import unittest

class BinaryTree:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class Solution:
    def __init__(self):
        self.count=0
        self.n=0
    def find_num_k_node(self,root,n):
        self.count=0
        self.n=n
        if root is None:
            return None
        data=self.traverse(root)
        if data is not None:
            return data.data
        else:
            return None

    def traverse(self,root:BinaryTree):
        if root.left is not None:
            self.traverse(root.left)
        self.count+=1
        if self.count==self.n:
            return root
        if root.right is not None:
            self.traverse(root.right)





class Test(unittest.TestCase):
    obj=Solution()
    def test_1(self):
        bt2=BinaryTree(2)
        bt3=BinaryTree(3)
        bt4=BinaryTree(4)
        bt5=BinaryTree(5)
        bt6=BinaryTree(6)
        bt7=BinaryTree(7)
        bt8=BinaryTree(8)
        bt5.left=bt3
        bt5.right=bt7
        bt3.left=bt2
        bt3.right=bt4
        bt7.left=bt6
        bt7.right=bt8
        self.assertEqual(self.obj.find_num_k_node(bt5,4),5 )

    def test_2(self):
        self.assertEqual("", "")

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
