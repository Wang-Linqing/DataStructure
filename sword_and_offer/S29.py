class Solution:
    @staticmethod
    def traversal(mat):
        if mat is None:
            return
        rows=len(mat)
        cols=len(mat[0])
        row=0
        col=0
        count=rows*cols
        tmp=0
        _cols=cols
        _rows=rows
        while True:
            if _rows==1:
                for i in range(col,_cols+(cols-_cols)//2):
                    print(mat[row][i])
                break
            if _cols==1:
                for i in range(row,_rows+(rows-_rows)//2):
                    print(mat[i][col])
                break
            if _cols ==0 and _rows==0:
                break
            while row==(rows-_rows)//2:
                while col <=cols-(cols-_cols)//2-1:
                    print(mat[row][col])
                    col+=1
                col-=1
                row+=1
            while col==cols-(cols-_cols)//2-1:
                while row <=rows-(rows-_rows)//2-1:
                    print(mat[row][col])
                    row+=1
                row-=1
                col-=1
            while row==rows-(rows-_rows)//2-1:
                while col>=(cols-_cols)//2:
                    print(mat[row][col])
                    col-=1
                col+=1
                row-=1
            while col==(cols-_cols)//2:
                while row>=(rows-_rows)//2+1:
                    print(mat[row][col])
                    row-=1
                row+=1
                col+=1
            _rows-=2
            _cols-=2


a=[[1,2,3,4]]
Solution.traversal(a)