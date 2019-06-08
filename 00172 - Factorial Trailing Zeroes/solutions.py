class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        
        div = 5
        
        while (n/div >= 1):
            res += int(n/div)
            div *= 5
        
        return res
        
