class Solution():
    count=0
    @staticmethod
    def is_satisfied(rows,cols,row,col,k):
        if row >=0 and row<rows and col>=0 and col<cols and k>=0:
            sum=0
            tmp=row
            while tmp>0:
                sum=sum+tmp%10
                tmp=tmp//10
            tmp=col
            while tmp>0:
                sum=sum+tmp%10
                tmp=tmp//10
            if sum<=k:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def next_path(visited, rows, cols, row, col, k):
        if row>rows-1 or col>cols-1 or row <0 or col <0:
            return 0
        count=0
        if visited[row][col] ==0:
            if Solution.is_satisfied(rows,cols,row,col,k):
                visited[row][col]=1
                count=1+Solution.next_path(visited,rows,cols,row+1,col,k)+Solution.next_path(visited,rows,cols,row-1,col,k)+Solution.next_path(visited,rows,cols,row,col+1,k)+Solution.next_path(visited,rows,cols,row,col-1,k)
            else:
                visited[row][col]=1
        return count

    @staticmethod
    def count_moving(rows,cols,k):
        if not(rows>0 and cols>0 and k>=0):
            return 0
        visited=[]
        satifi=[]
        Solution.count=0
        for i in range(0,rows):
            tmp=[]
            t=[]
            for j in range(0,cols):
                tmp.append(0)
                t.append(False)
            visited.append(tmp)
            satifi.append(tmp)
        count=Solution.next_path(visited,rows,cols,0,0,k)
        for i in visited:
            print(i)
        for i in range(0,rows):
            for j in range(0,cols):
                satifi[i][j]=Solution.is_satisfied(rows,cols,i,j,k)
        for i in satifi:
            print(i)

        return count



print(Solution.count_moving(100,100,0))