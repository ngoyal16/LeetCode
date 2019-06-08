class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        fibs = [0, 1]
        
        i = 1
        while i < n + 1:
            fibs.append(fibs[i] + fibs[i-1])
            i = i + 1
        
        return fibs[n + 1]
        
