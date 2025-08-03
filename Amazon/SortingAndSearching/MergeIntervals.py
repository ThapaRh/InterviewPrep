def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    '''
    [[1,3],[2,6],[8,10],[15,18]]
    first I would sort by first element
    
    2<=3:yes
    1,max(3,6) = [1,6]
    stack: ordered by descending order
    pop the compare with last elem : pop vs stack[-1]
    TC: O(nlogn)
    SC: I think it's constant
    '''
    
    intervals.sort(key=lambda x:x[0],reverse=True)
    final = []
    while(intervals):
        [i,j] = intervals.pop()
        if len(intervals)>0:
            if intervals[-1][0]<j:
                [i2,j2] = intervals.pop()
                start = i
                end = max(j,j2)
                intervals.append([start,end])
                continue
        final.append([i,j])
    return final
    