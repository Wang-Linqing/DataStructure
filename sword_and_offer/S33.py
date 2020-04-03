class BinaryTree:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def verify_squence_of_BST(sequence):
        if sequence is None:
            return False
        if len(sequence) == 0:
            return True
        tmp = sequence.pop()
        left = []
        right = []
        index = -1
        for i, item in enumerate(sequence):
            if item < tmp:
                left.append(i)
                if index>=0:
                    return False
            else:
                index = i
                right.append(item)

        return Solution.verify_squence_of_BST(left) and Solution.verify_squence_of_BST(right)


print(Solution.verify_squence_of_BST([5, 7, 6, 9, 11, 10, 8]))
print(Solution.verify_squence_of_BST([7,4,6,5]))
