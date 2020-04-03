
class BinaryTreeNode(object):
    def __init__(self,data=0,l_tree=None,r_tree=None):
        self.data=data
        self.l_tree=l_tree
        self.r_tree=r_tree

class Solution:
    @staticmethod
    def rebuild_binary_tree(pre,mid):
        print(pre,mid)
        if len(pre)==0:
            return None
        elif len(pre)==1:
            root = BinaryTreeNode(pre[0])
            return root
        else:
            root=BinaryTreeNode(pre[0])
            index=mid.index(pre[0])
            if index==0:
               l_pre=[]
               l_mid=[]
            else:
                l_pre=pre[1:index+1]
                l_mid=mid[0:index]
            root.l_tree=Solution.rebuild_binary_tree(l_pre,l_mid)
            if index==len(mid)-1:
                r_pre=[]
                r_mid=[]
            else:
                r_pre=pre[index+1:]
                r_mid=mid[index+1:]
            root.r_tree=Solution.rebuild_binary_tree(r_pre,r_mid)
            return root
mpre=[1,2,4,7,3,5,6,8]
mmid=[4,7,2,1,5,3,8,6]
re=Solution.rebuild_binary_tree(mpre,mmid)
a=90
