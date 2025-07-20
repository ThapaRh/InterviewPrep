'''
This is a dp problem because we have to find maximum money we can make by robbing the house
'''
#The bottom up approach, we start from beginning and build on top of that
#TC: O(N)
#SC=O(N)
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        options: rob or dont rob
        if rob: next current+2
        not rob: next curr+1 or current+2
        '''
        max_money = [nums[j] for j in range(len(nums))]
        for i in range(1,len(nums)):
            if i == 1:
                max_money[i] = max(max_money[i-1],max_money[i])
            else:
                rob_curr = max_money[i-2] + max_money[i]
                max_money[i] = max(rob_curr,max_money[i-1])
        return max_money[len(nums)-1]
    
#the top down approach
#TC: O(N)
#SC=O(N)
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        def calculate_max_money(i,cache):
            if i<0:
                return 0
            if i==0:
                return nums[i]
            if i in cache:
                return cache[i]
            cache[i] = max(nums[i]+calculate_max_money(i-2,cache),calculate_max_money(i-1,cache))
            return cache[i]
        return calculate_max_money(length-1,{})