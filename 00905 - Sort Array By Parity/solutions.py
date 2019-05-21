class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        res = []
        
        for num in A:
            if num % 2:
                res.append(num)
            else:
                res.insert(0, num)
        
        return res
