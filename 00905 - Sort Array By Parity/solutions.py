class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        oddList = []
        evenList = []
        
        for num in A:
            if num % 2:
                oddList.append(num)
            else:
                evenList.append(num)
        
        return evenList + oddList
