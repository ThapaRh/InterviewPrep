class MedianFinder:
    '''
    1,2,7,3,1
    
    max_heap= 1,2
    min_heap= 
    check_length
    max_heap = 1
    min_heap = 2
    
    max = 1,7
    min = 2
    
    check for max_heap<min_heap:
    no? - balance from left to right
    
    check for length:
    no? remove from whatever is longer and balance
    
    left = []
    right = []
    
    add to left
    check is max_left<min_right if min_right.length >0
    no?
    add_to_heap(right_heap,popfromleft)
    
    check if two heaps are balanced: l1-l2<=1:
    no?
    if l1>l2:
    add_to_heap(right_heap,popfromleft)
    else:
    add_to_heap(left_heap,popfromright)
    
    TC : O(logn) for each input
    SC: O(n)
    '''

    def __init__(self):
        self.left = [] #max_heap
        self.right = [] #min_heap
        heapq.heapify(self.left)
        heapq.heapify(self.right)
    
    def add_to_heap(self,arr,element):
        heapq.heappush(arr,element)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left,-1*num)
        if self.right:
            if self.left[0]*-1 > self.right[0]:#checking if max_left<min_right
                element = heapq.heappop(self.left)*-1
                self.add_to_heap(self.right,element)
        l1 = len(self.left)
        l2 = len(self.right)
        if abs(l1-l2)>1:
            if l1>l2:
                elem = heapq.heappop(self.left)*-1
                self.add_to_heap(self.right,elem)
            else:
                elem = heapq.heappop(self.right)*-1
                self.add_to_heap(self.left,elem)            

    def findMedian(self) -> float:
        l1 = len(self.left)
        l2 = len(self.right)
        if (l1>l2):
            return -1*self.left[0]
        elif l2>l1:
            return self.right[0]
        else:
            return (-1*self.left[0]+self.right[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()