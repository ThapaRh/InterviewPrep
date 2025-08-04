def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
    '''
    i = 1
    -1,+1
    if same update i, i+=1
    
    '''
    for j in range(n):
        i = 1
        prev = cells[0]
        while(i<len(cells)):
            if i==len(cells)-1:
                cells[i] = 0
                i==1
                continue
            new_prev = cells[i]
            if prev == cells[i+1]:
                cells[i] = 1
            else:
                cells[i] = 0
            prev = new_prev
    
                