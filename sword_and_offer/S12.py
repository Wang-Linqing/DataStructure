

def have_next(mat,rows,cols,visted,row,col,path,index):
    print(visted)
    if index==len(path)-1:
        return True
    if mat[row][col]!=path[index]:
        index-=1
        visted[row][col]=False
        return False
    visted[row][col]=True
    has_path=False
    index+=1
    if row-1>=0 and visted[row-1][col] is False:
        ret_up=have_next(mat,rows,cols,visted,row-1,col,path,index)
        has_path=has_path or ret_up
    if row + 1 <= rows - 1 and visted[row + 1][col] is False:
        ret_d = have_next(mat, rows, cols, visted, row + 1, col, path, index)
        has_path = has_path or ret_d
    if col-1>=0 and visted[row][col-1] is False:
        ret_l=have_next(mat,rows,cols,visted,row,col-1,path,index)
        has_path=has_path or ret_l
    if col+1<=cols-1 and visted[row][col+1] is False:
        ret_r=have_next(mat,rows,cols,visted,row,col+1,path,index)
        has_path=has_path or ret_r
    if has_path is False:
        index-=1
        visted[row][col]=False
    return has_path


def is_path(mat,path):
    if mat is None:
        return False
    if path is None:
        return False
    rows=len(mat)
    cols=len(mat[0])
    visited=[]
    for i in range(0,rows):
        tmp=[]
        for j in range(0,cols):
            tmp.append(False)
        visited.append(tmp)
    for i in range(0,rows):
        for j in range(0,cols):
            if have_next(mat,rows,cols,visited,i,j,path,0):
                return True
    return False
S=[
    ["a","b","t","g"],
    ["c","a","c","a"],
    ["j","g","e","f"],
   ]
print(is_path(S,"abtcafegacj"))



