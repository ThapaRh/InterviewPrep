
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         '''
#         Input: nums = [3,0,1]
#         Output: 2
#         no extra sppace and O(n) TC: hmm interesting
#                t
#         nums = 3,0,1,*
#                0,1,2,3
#                i
#         while(i<length):
#         if nums[i]!=i:
#         temp = nums[i]
#         nums[i] = nums[temp]
#         nums[temp] = temp
#         [-1,6,4,2,3,5,7,0,1,9]
#         '''
#         nums.append(-1)
#         length = len(nums)
#         i = 0
#         while(i<length):
#             if nums[i]!=i:
#                 temp = nums[i] #1
#                 nums[i] = nums[temp] #
#                 nums[temp] = temp #
#             i+=1
#         j = 0
#         print(nums)
#         while(j<length):
#             if nums[j]==-1:
#                 return j
#             j+=1

#all this effing failed just for me to realize the solution is this bitch
        n = len(nums)
        expected_sum = n*(n+1)//2
        curr_sum = sum(nums)
        return expected_sum - curr_sum
#I miight just puke wtf
