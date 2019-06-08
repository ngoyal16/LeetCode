class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n < 1:
            return False
        
        return (sum([int(i) for i in list(bin(n).replace("0b",""))])) == 1
