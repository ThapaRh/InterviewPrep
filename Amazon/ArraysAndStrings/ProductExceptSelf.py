class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        prefix sum
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        
        [1,1,1,1]
        [1,1,2,6]
        
        [24,12,4,1]
        
        TC = O(n)
        SC = O(1) //excluding the space to store the output
        '''
        length = len(nums)
        final = [1 for i in range(length)]
        i = 1
        while(i<length):
            final[i]*=final[i-1]*nums[i-1]
            i+=1
        j = length-2
        temp = 1
        while(j>=0):
            temp *=nums[j+1] #1*4 = 4 4*3=12 12*2 = 24
            final[j]*=temp
            j-=1
        return final
