'''
looks like i do simple dfs
r,c
dfs(r,c):
base 
if grid[r][c]!=0:
    grid[r][c]=0
    r+1,c+1,r-1,c-1 
    TC: n*m
    SC=n*m
'''

def number_islands(grid):
    row = len(grid)
    col = len(grid[0])
    number_of_islands = 0
    
    def dfs_search(r,c):
        if r<0 or c<0 or r>=row or c>=row or grid[r][c]=="0":
            return
        grid[r][c]="0"
        dfs_search(r+1,c)
        dfs_search(r-1,c)
        dfs_search(r,c+1)
        dfs_search(r,c-1)
        
        
    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1":
                dfs_search(i,j)
                number_of_islands+=1
    return number_of_islands