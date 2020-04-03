class BinaryTree:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:

    @staticmethod
    def print_tree(root):
        if root is None:
            return
        queue=[]
        queue.append(root)
        count=0
        while len(queue)>0:
            length=len(queue)
            for i in range(0,length):
                tmp=queue[i]
                if tmp.left is not None:
                    queue.append(tmp.left)
                if tmp.right is not None:
                    queue.append(tmp.right)
            if count%2==0:
                for i in range(0,length):
                    print(queue.pop(0).data,end=" ")
                count+=1
                print("")
            else:
                for i in range(0,length):
                    print(queue.pop(length-i-1).data,end=" ")
                count+=1
                print("")


root = BinaryTree(8, BinaryTree(6, BinaryTree(5), BinaryTree(7)), BinaryTree(10, BinaryTree(9), BinaryTree(11)))
Solution.print_tree(root)