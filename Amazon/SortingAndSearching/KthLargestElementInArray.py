from collections import heapq
def findKthLargest(self, nums: List[int], k: int) -> int:
    '''
    TC=O(nlogk)
    SC = O(1ß)
    '''
    nums = -1*nums
    heapq.heapify(nums)
    while(nums and k):
        ret = heapq.heappop(nums)
        k-=1
        if k == 0:
            return -1*ret
    return ValueError("test case error")
        