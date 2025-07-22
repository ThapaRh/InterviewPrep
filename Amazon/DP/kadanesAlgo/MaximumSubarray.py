'''
This is kadane's algorithm, very simple
TC : O(N)
SC:O(1)
'''

class Solution:
    def maxSubArray(self, nums):
        #[-2,1,-3,4,-1,2,1,-5,4]
        final_max = nums[0]
        curr_max = nums[0]
        if len(nums)==1:
            return curr_max
        for i in range(1,len(nums)):
            if nums[i]+curr_max>nums[i]:
                curr_max+=nums[i]
            else:
                curr_max=nums[i]
            final_max = max(final_max,curr_max)
        return final_max
    
test = Solution()
print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))