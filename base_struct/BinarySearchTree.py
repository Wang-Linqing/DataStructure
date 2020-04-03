class BinaryTree(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def list_to_binary_search_tree(data: list) -> BinaryTree:
        if data is None:
            return None
        if len(data) == 0:
            return None
        root = BinaryTree(data[0])
        for item in data[1:]:
            Solution.bulid_binary_search_tree(root, item)
        return root

    @staticmethod
    def bulid_binary_search_tree(root, data):
        if data is None:
            return
        if root is None:
            raise ValueError
        if data < root.data:
            if root.left is None:
                root.left = BinaryTree(data)
            else:
                Solution.bulid_binary_search_tree(root.left, data)
        else:
            if root.right is None:
                root.right = BinaryTree(data)
            else:
                Solution.bulid_binary_search_tree(root.right, data)
    @staticmethod
    def find_element_in_binary_search_tree(root,data):
        if root is None:
            return None
        if data is None:
            return None
        return Solution.search(root,data)
    @staticmethod
    def search(root,data):
        if root.data==data:
            return root
        elif root.data>data:
            if root.left is None:
                return None
            else:
                return Solution.search(root.left,data)
        else:
            if root.right is None:
                return None
            else:
                return Solution.search(root.right,data)
