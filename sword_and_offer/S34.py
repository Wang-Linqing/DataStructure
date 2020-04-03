class BinaryTree:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def print_all_path_sum_N(root,N):
        if root is None:
            return
        if N is None:
            return
        path=[]
        Solution.travesal(path,root,0,N)
    @staticmethod
    def travesal(path,root,current_sum,N):
        if root.left is None and root.right is None:
            if current_sum+root.data==N:
                for i in path:
                    print(i.data,end=" ")
                print(root.data)
            return

        path.append(root)
        tmp=current_sum+root.data
        if root.left is not None:
            Solution.travesal(path,root.left,tmp,N)
        if root.right is not None:
            Solution.travesal(path,root.right,tmp,N)
        path.pop()


root = BinaryTree(10, BinaryTree(5, BinaryTree(4), BinaryTree(7)), BinaryTree(12))
Solution.print_all_path_sum_N(root,22)