'''
https://leetcode.com/problems/unique-paths-ii/
'''
#we will be doing bottom up approach first 
#basically doing backtracking and adding memoization

#TC: O(m*n) SC = O(m*n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        dp problem
        cache = [-1*col for i in range(row)]
        start from 0,0
        if grid[x][y] == 1:
            return 0
        if cache[x][y]!=-1:
            return cache[x][y]
        r_r = dfs(r+1,c)
        r_l = dfs(r,c+1)
        cache[x][y] = 1+r_r if r_r != 0 else 0 + 1+r_l if r_l != 0 else 0
        return cache
        example:
        [ 2, 1, 1]
        [ 1, 1, 1] //visualizing with example makes coding and debugging so much easier
        [ 1, 1,-1]
        00
        01
        [-1,-1]
        [-1,-1]
        '''
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        cache = [[-1]*col for i in range(row)]
        if obstacleGrid[row-1][col-1] == 1: #make sure to not forget the edge cases
            return 0
        def dp(r,c):
            print(r,c)
            if r==row-1 and c==col-1:#had issues here where I checked for r>=row and c>=col instead of the last element, our last element is the endpoint/destination
                return 1
            if r>=row or c>=col:
                return 0
            if obstacleGrid[r][c]==1:
                return 0
            if cache[r][c]!=-1:
                return cache[r][c]
            right_val = dp(r+1,c)
            left_val = dp(r,c+1)
            print(right_val,left_val)
            cache[r][c] = right_val + left_val 
            return cache[r][c]
        return dp(0,0)
    
    
    #bottom up approach

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        dp problem
        cache_array = [m+1*n+1] #everything 0
        [0 0 0 0]
        [0 0 0 0]
        [0 0 0 0]
        [0 0 0 0]
        cache_array[1][1] = 1
        for i in range(1,row+1):
            for j in range(1,col+1):
                if i==j==1:
                    continue
                cache_array[i][j] = cache_array[i-1][j] + cache_array[i][j-1]
        return cache_array[row][col]
        '''
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[row-1][col-1]==1 or obstacleGrid[0][0]==1:#with bottom up we have to be careful of few more edge cases, this is question to ask interviewer
            return 0
        cache_array = [[0]*(col+1) for k in range(row+1)]
        cache_array[1][1] = 1
        for i in range(1,row+1):
            for j in range(1,col+1):
                if i==j==1:
                    continue
                if obstacleGrid[i-1][j-1]==1:
                    continue
                cache_array[i][j] = cache_array[i-1][j] + cache_array[i][j-1]
        return cache_array[row][col]
