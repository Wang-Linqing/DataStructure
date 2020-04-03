class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
class Solution:
    @staticmethod
    def reverse_list(head):
        if head is None:
            return None
        if head.next is None:
            return head
        p_pre=head
        p_post=head.next
        while p_post.next is not None:
            print(p_pre.data,p_post.data)
            tmp = p_post.next
            p_post.next=p_pre
            p_pre=p_post
            p_post=tmp

        head.next=None
        p_post.next=p_pre
        return p_post
header=Node(1)
p=header
for i in range(2,3):
    p.next=Node(i)
    p=p.next
ret=Solution.reverse_list(header)
print(ret.data)
print("#################")
p=ret
while p is not  None:
    print(p.data)
    p=p.next
