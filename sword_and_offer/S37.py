class BinaryTree:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
class Solution:
    sequence=[]
    @staticmethod
    def serialize(root):
        if root is None:
            return None
        Solution.sequence.clear()
        Solution.traverse(root)
        string=""
        for item in Solution.sequence:
            string+=item+","
        string=string[0:-1]
        return string
    @staticmethod
    def traverse(root):
        if root is None:
            Solution.sequence.append("$")
            return
        Solution.sequence.append(str(root.data))
        Solution.traverse(root.left)
        Solution.traverse(root.right)
    @staticmethod
    def deserialize(string):
        if string is None:
            return None
        data_list=string.split(",")
        return Solution.de_traverse(data_list)
    @staticmethod
    def de_traverse(data_list):

        if data_list[0]=="$":
            tree_node=None
            data_list.pop(0)
            return tree_node
        else:
            tree_node = BinaryTree(data_list.pop(0))
        tree_node.left=Solution.de_traverse(data_list)
        tree_node.right=Solution.de_traverse(data_list)
        return tree_node

root = BinaryTree(1, BinaryTree(2, BinaryTree(4)), BinaryTree(3,BinaryTree(5),BinaryTree(6)))
ret=Solution.serialize(root)
print(ret)
ret=Solution.deserialize(ret)
ret=Solution.serialize(ret)
print(ret)


