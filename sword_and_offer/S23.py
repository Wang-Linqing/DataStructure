class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next

class Solution:
    @staticmethod
    def find_loop_in_door(header):
        if header is None:
            return None
        p_slow=header
        p_fast=header
        has_loop=False
        while p_fast.next is not None:
            p_fast=p_fast.next
            if p_fast==p_slow:
                has_loop=True
                break
            else:
                if p_fast.next is None:
                    break
                else:
                    p_fast=p_fast.next
                    if p_fast==p_slow:
                        has_loop=True
                        break
                    else:
                        p_slow=p_slow.next
        if not has_loop:
            return None
        p_node=p_slow.next
        count=1
        while p_node !=p_slow:
            p_node=p_node.next
            count+=1
        print(count)
        p_node=header
        p_in_door=header
        tmp=1
        while tmp<count:
            p_node=p_node.next
            tmp+=1
        while p_in_door!=p_node.next:
            p_in_door=p_in_door.next
            p_node=p_node.next
        return p_in_door

header=Node(1)
p=header
tmp=None
for i in range(2,1000):
    p.next=Node(i)
    p=p.next
    if i==90:
        tmp=p
p.next=tmp
ret=Solution.find_loop_in_door(header)
if ret is not None:
    print(ret.data)
else:
    print(ret)