class TicTacToe:
    '''
    X X X
    X X X
    X X X
    
    set_row 3
    sel_col 3 
    
    row = [{}*3]
    col = [{}*3]
    diagonal = [{}*2]
    
    if user in row[i]:
    row[i][user]+=1
    
    '''
    def __init__(self,n):
        self.row_d = [{}*n]
        self.col_d = [{}*n]
        self.diag_d = [{}*2]
        self.n = n
    
    def move(self,row,col,player):
        if player in self.row_d[row]:
            self.row_d[row][player]+=1
            if self.row_d[row][player]==self.n:
                return player
        else:
            self.row_d[row][player]=1
        if player in self.col_d[col]:
            self.col_d[col]+=1
            if self.col_d[col][player]==3:
                return player
        else:
            self.col_d[col]=1
        '''
        00 01 02 03
        10 11 12 13
        20 21 22 23
        30 31 32 33
        '''
        
            
            
        
            
            
        
        