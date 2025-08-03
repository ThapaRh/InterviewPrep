def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    '''
    [[3,3],[5,-1],[-2,4]]
    calculate the distance and add to array [d,x,y] then sort it and return top k
    or i can put in a heap
    '''
    distance = []
    for x,y in points:
        d = x**2+y**2
        distance.append([d,x,y])
    distance.sort(key=lambda x:x[0])
    final = []
    i = 0
    while(i<k):
        d,x,y = distance[i]
        final.append([x,y])
        i+=1
    return final