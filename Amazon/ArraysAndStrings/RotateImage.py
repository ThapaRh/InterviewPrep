class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        1,2,3,4
        
        TC=O(n^2)
        SC=O(1) --no extra space used
        
        Tip: visualize the rotating of matrix corners from 4 corners and another 4 corners and so on
        """
        top = 0
        bottom = len(matrix)-1
        while(top<bottom):
            l = top
            r = bottom
            for i in range(0,r-l): #because we only need to rotate r-l times
                #saving the topleft in variable
                temp = matrix[top][l+i]
                
                #bottomleft to topleft
                matrix[top][l+i] = matrix[bottom-i][l]
                
                #bottomright to bottomleft
                matrix[bottom-i][l] = matrix[bottom][r-i]
                
                #topright to bottomright
                matrix[bottom][r-i] = matrix[top+i][r]
                
                #curr to topleft
                matrix[top+i][r] = temp
            top+=1
            bottom-=1
