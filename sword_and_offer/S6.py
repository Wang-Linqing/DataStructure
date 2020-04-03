class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next

class Solution:
    @staticmethod
    def print_revers(head):
        if head.next is not None:
            Solution.print_revers(head.next)
        print(head.data)
a=Node(1)
b=Node(2)
c=Node(3)
a.next=b
b.next=c
Solution.print_revers(a)