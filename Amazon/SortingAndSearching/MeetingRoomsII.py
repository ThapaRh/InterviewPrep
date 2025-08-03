def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    '''
    0,30 0,30    5,10   15,20    6,16
    
    we check to see in our heap if we have any meeting rooms which ends before our new starts...
    if yes we dont add rooms we update new end time
    if not we add new end time to heap and add one more meeting room
    
    TC: nlogn
    SC:n
    '''
    
    intervals.sort(key=lambda x:x[0])
    available_time = []
    heapq.heapify(available_time)
    meeting_rooms = 0
    for start,end in intervals:
        if available_time and available_time[0]<=start:
                heapq.heappop(available_time)
        else:
            meeting_rooms+=1
        heapq.heappush(available_time,end)
    return meeting_rooms
                
                
                