def search(self, nums: List[int], target: int) -> int:
    '''
    4,5,6,7,0,1,2
    
    7>4 and 7<2: false
    0,2
    1>0 and 1<2:
    True
    
    0
    
    use binary search to find smallest i.e the pivot and do two binary search in two sorted ordered half
    
    78123456
    '''
    low = 0
    high = len(nums) - 1
    while(low<=high):
        mid = (low+high)//2
        if nums[mid]>nums[-1]:
            low = mid+1
        else:
            high = mid-1
    pivot = low
    
    #binary search in left and right halves
    def binary_search(left,right):
        if target<nums[0] and target>nums[-1]:
            return -1
        while(left<=right):
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target>nums[mid]:
                left = mid+1
            else:
                right = mid-1 #made a mistake here, updated left instead of updating right
        return -1
    
    val1 = binary_search(0,pivot-1) 
    val2 = binary_search(pivot,len(nums)-1)
    if val1==-1 and val2==-1:
        return -1
    else:
        return val1 if val1!=-1 else val2
    
                
            
    
    