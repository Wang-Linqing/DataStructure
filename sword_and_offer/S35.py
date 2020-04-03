class Node:
    def __init__(self,data=0,next=None,sibling=None):
        self.data=data
        self.next=next
        self.sibling=sibling

class Solution:
    @staticmethod
    def copy(head):
        if head is None:
            return head
        p=head
        while p is not None:
            node=Node(p.data)
            tmp=p.next
            p.next=node
            node.next=tmp
            p=node.next
        p=head
        while p is not None:
            node=p.next
            if p.sibling is not None:
                node.sibling=p.sibling.next
            p=node.next
        p=head
        new_head=p.next
        p=head
        q=p.next
        while q.next is not None:
            p.next=q.next
            p=q.next
            q.next=p.next
            q=p.next
        return new_head
a1=Node(1)
a2=Node(2)
a3=Node(3)
a4=Node(4)
a5=Node(5)
a6=Node(6)
a7=Node(7)
# a1.next=a2
# a2.next=a3
# a3.next=a4
# a4.next=a5
# a5.next=a6
# a6.next=a7
# a1.sibling=a7
# a4.sibling=a1
# a3.sibling=a5
a1.next=a2
a2.sibling=a1
a1.sibling=a2
p=a1
while p is not None:
    if p.sibling is not None:
        print(p.data,p.sibling.data)
    else:
        print(p.data)
    p=p.next
ret=Solution.copy(a1)
p=ret
while p is not None:
    if p.sibling is not None:
        print(p.data,p.sibling.data)
    else:
        print(p.data)
    p=p.next




