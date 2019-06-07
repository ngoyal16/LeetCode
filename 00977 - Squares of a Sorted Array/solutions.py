class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        return map(lambda x: x * x, sorted(A, key=abs))
