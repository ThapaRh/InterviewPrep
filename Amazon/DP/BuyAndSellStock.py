'''
Tc=O(n)
Sc=O(1)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Input: prices = [7, 1,  5,  3,  6,  4]
                        b/s b/s s       s
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
        '''
        buy = sell = 0
        if len(prices)==1:
            return 0
        i = 1
        profit = 0
        while(i<len(prices)):
            if prices[i]<prices[buy]:
                buy = i
                sell = i
            if prices[i]>prices[sell]:
                sell = i
                profit = max(prices[sell] - prices[buy], profit)
            i+=1
        return profit