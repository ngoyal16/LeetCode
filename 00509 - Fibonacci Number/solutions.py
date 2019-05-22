class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        fibs = [0, 1]
        
        i = 1
        while i < N:
            fibs.append(fibs[i] + fibs[i-1])
            i = i + 1
        
        return fibs[N]
        
