class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        TC: O(N)
        SC: O(1)
        
        MaxLeft and MaxRightArray
        better: two pointer
        '''
        length = len(height)
        left_height = [0 for i in range(length)]
        right_height = [0 for i in range(length)]
        
        # i = 1
        # while(i<length):
        #     if height[i-1]>left_height[i-1]:
        #         left_height[i] = height[i-1]
        #     else:
        #         left_height[i] = left_height[i-1]
        #     i+=1
        # j = length-2
        # while(j>=0):
        #     if height[j+1]>right_height[j+1]:
        #         right_height[j] = height[j+1]
        #     else:
        #         right_height[j] = right_height[j+1]
        #     j-=1
        # k = 0
        # total = 0
        # while(k<length):
        #     water = min(left_height[k],right_height[k]) - height[k]
        #     if water>0:
        #         total+=water
        #     k+=1
        # return total
        
        #we wont need to use extra space if we keep in mind that we care about minimum of the maximumleft and maximum right
        i = 0
        j = len(height)-1
        max_left = height[0]
        max_right = height[-1]
        total = 0
        #iterating till the crossovers
        while(i<j):
            if max_left<max_right:
                #we move the index of lower height side and test that index
                i+=1
                max_left = max(max_left,height[i])#update max_left if curr height is greater
                total+=max_left-height[i] #if our curr height is the max then we add 0
            else:
                j-=1
                max_right = max(max_right,height[j])
                total+=max_right-height[j]
        return total
                
                    
                    
                
            
    
class Main:
    result = Solution()
    print(result.trap())