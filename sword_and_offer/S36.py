class BinaryTree:
    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

class Solution:

    @staticmethod
    def convert_BST_to_link_list(root):
        if root is None:
            return None
        sequence=[]
        Solution.traverse(root,sequence)
        head=sequence[0]
        head.left=None
        for i in range(0,len(sequence)-1):
            sequence[i].right=sequence[i+1]
            sequence[len(sequence)-i-1].left=sequence[len(sequence)-i-2]
        sequence[-1].right=None
        return head
    @staticmethod
    def traverse(root,sequence):
        if root.left is not None:
            Solution.traverse(root.left,sequence)
        sequence.append(root)
        if root.right is not None:
            Solution.traverse(root.right,sequence)
    @staticmethod
    def convert_BST_to_link_list_without_stack(root):
        if root is None:
            return None





root = BinaryTree(8, BinaryTree(6, BinaryTree(5), BinaryTree(7)), BinaryTree(10, BinaryTree(9), BinaryTree(11)))
ret=Solution.convert_BST_to_link_list(root)
p=ret
while p is not None:
    print(p.data)
    p=p.right