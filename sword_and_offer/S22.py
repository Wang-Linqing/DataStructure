class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next


class Solution:
    @staticmethod
    def get_Kth_node_from_the_bottom(header,k):
        if header is None:
            return None
        tmp=1
        p=header
        while tmp<k:
            if p.next is None:
                return None
            else:
                p=p.next
                tmp+=1
        print(tmp)
        p_k=header
        while p.next is not None:
            p=p.next
            p_k=p_k.next
        return p_k
header=Node(1)
p=header
for i in range(2,20):
    p.next=Node(i)
    p=p.next
print(p.data)
print(Solution.get_Kth_node_from_the_bottom(header,1).data)



