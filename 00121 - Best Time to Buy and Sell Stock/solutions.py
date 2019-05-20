class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        length = len(prices)
        
        if length <= 1:
            return 0
        
        
        maxProfit = 0
        minPrice = prices[0]
        
        for i in range(length):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)
        
        return maxProfit
