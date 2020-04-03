class BinaryTree:
    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

class Solution:
    last_node=None
    @staticmethod
    def convert_BST_to_link_list(root):
        if root is None:
            return None
        Solution.traverse(root)
        head=Solution.last_node
        while head.left is not None:
            head=head.left

        return head
    @staticmethod
    def traverse(root):
        if root is None:
            return
        tmp=root
        if tmp.left is not None:
            Solution.traverse(tmp.left)
        tmp.left=Solution.last_node
        if Solution.last_node is not None:
            Solution.last_node.right=tmp
        Solution.last_node=tmp
        if tmp.right is not None:
            Solution.traverse(tmp.right)

root = BinaryTree(8, BinaryTree(6, BinaryTree(5), BinaryTree(7)), BinaryTree(10, BinaryTree(9), BinaryTree(11)))
ret=Solution.convert_BST_to_link_list(root)
p=ret
while p is not None:
    print(p.data)
    p=p.right



