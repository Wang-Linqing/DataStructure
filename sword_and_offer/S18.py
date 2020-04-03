class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    @staticmethod
    def remove_node(header, node):
        if header is None or node is None:
            return Node
        if header == node:
            return node.next
        else:
            if node.next is None:
                p = header
                while p.next != node and p.next is not None:
                    p = p.next
                if p.next is None:
                    return header
                else:
                    p.next = p.next.next
                    del node
            else:
                tmp = node.next
                node.data = node.next.data
                node.next = node.next.next
                del tmp

    @staticmethod
    def remove_same_node(header):
        if header is None:
            return None
        pre_node = None
        p_node = header
        ret=header
        while p_node.next is not None:
            print(p_node.data)
            if p_node.next.data == p_node.data:
                data = p_node.data
                while p_node is not None:
                    if p_node.data == data:
                        p_node = p_node.next
                    else:
                        break
                if pre_node is None:
                    ret=p_node
                else:
                    pre_node.next = p_node
                if p_node is None:
                    break


            else:
                pre_node = p_node
                p_node = p_node.next
        return ret
header=Node(-1)
p=header
for i in range(20):
    p.next=Node(i)
    p=p.next
p=header
p.next.data=1
p.next.next.data=1
p.next.next.next.data=1
p=header
header.data=-1
while p is not None:
    print(p.data)
    p=p.next
p=header
p=Solution.remove_same_node(header)
print(" ################## ")
while p is not None:
    print(p.data)
    p=p.next