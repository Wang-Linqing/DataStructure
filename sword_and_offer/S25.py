class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
class Solution:
    @staticmethod
    def merge(head_1,head_2):
        if head_1 is None:
            return head_2
        if head_2 is None:
            return head_1
        p_1=head_1
        p_2=head_2
        if p_1.data<p_2.data:
            head=p_1
        else:
            head=p_2
        while p_1 is not None and p_2 is not None:
            if p_1.data<=p_2.data:
                while p_1.next is not None:
                    if p_1.next.data<=p_2.data:
                        p_1=p_1.next
                    else:
                        break
                if p_1.next is not None:
                    tmp_1=p_1.next
                    tmp_2=p_2.next
                    p_1.next=p_2
                    p_2.next=tmp_1
                    p_1=p_2
                    p_2=tmp_2
                else:
                    p_1.next=p_2
                    break
            else:
                tmp_1=p_1.next
                tmp_2=p_2.next
                p_2.next=p_1
                p_2=tmp_2
        return head

header=Node(1)
p=header
tmp=None
for i in range(2,10,1):
    p.next=Node(i)
    p=p.next
header2=Node(-1)
p=header2
tmp=None
for i in range(1,30,3):
    p.next=Node(i)
    p=p.next
p=header
while p is not  None:
    print(p.data)
    p=p.next
p=header2
while p is not  None:
    print(p.data)
    p=p.next
p=header2
p.next.data=1
p.next.next.data=1
p.next.next.next.data=1
ret=Solution.merge(header,header2)
p=ret
print("#########################")
while p is not  None:
    print(p.data)
    p=p.next