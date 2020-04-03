
class BinaryTreeNode(object):
    def __init__(self,data=0,parent=None,l_tree=None,r_tree=None):
        self.data=data
        self.parent=parent
        self.l_tree=l_tree
        self.r_tree=r_tree

class Solution:
    @staticmethod
    def find_next_node_sorted_by_in_order_traversal(node):
        if node is None:
            return None
        if node.r_tree is not None:
            p=node.r_tree
            while p.l_tree is not None:
                p=p.l_tree
            return p.data
        elif node.parent is not None:
            current=node
            parent=node.parent
            while parent is not None:
                if parent.r_tree==current:
                    current=parent
                    parent=parent.parent
                else:
                    return parent.data
            return -1
        else:
            return -1


tree=BinaryTreeNode("a")
a=tree
b=BinaryTreeNode("b")
c=BinaryTreeNode("c")
d=BinaryTreeNode("d")
e=BinaryTreeNode("e")
f=BinaryTreeNode("f")
g=BinaryTreeNode("g")
h=BinaryTreeNode("h")
i=BinaryTreeNode("i")
tree.l_tree=b
tree.r_tree=c
b.parent=tree
b.l_tree=d
b.r_tree=e
c.parent=tree
c.l_tree=f
c.r_tree=g
d.parent=b
e.parent=b
e.l_tree=h
e.r_tree=i
f.parent=c
g.parent=c
h.parent=e
i.parent=e
print(tree)
order=[d,b,h,e,i,a,f,c,g]
print(Solution.find_next_node_sorted_by_in_order_traversal(g))



