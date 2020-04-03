S=[[1,2,8,9],
   [2,4,9,12],
   [4,7,10,13],
   [6,8,11,15],]
class Solution:
    @staticmethod
    def find(mat,num):
        if mat is None:
            return False
        if len(S)==0:
            return False
        row=len(S)
        col=len(S[0])
        l=0
        h=row-1
        if mat[0][0]>num:
            return False

        while l<=h:
            mid = (l + h) // 2
            if mat[0][mid]==num:
                return True
            elif mat[0][mid]<num:
                l=mid+1
            else:
                h=mid-1
        _row=0
        _col=h
        while _row<row and _col>0:
            if mat[_row][_col]==num :
                return True
            elif mat[_row][_col]<num:
                _row+=1
            else:
                _col-=1
        return False





for i in S:
    for j in i:
        print(j,Solution.find(S,j))
print(-1,Solution.find(S,-1))
print(100,Solution.find(S,100))
print(12,Solution.find(S,12))
print(1,Solution.find(S,1))
print(4,Solution.find(S,4))