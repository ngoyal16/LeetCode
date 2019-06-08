class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        
        lenA = len(A)
        lenS = len(A[0])
        
        res = 0
        
        for i in range(lenS):
            for j in range(lenA - 1):
                if ord(A[j][i]) > ord(A[j + 1][i]):
                    res += 1
                    break
        
        return res
