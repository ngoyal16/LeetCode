class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        addValue = 1
        rList = []
        
        for i in digits[::-1]:
            i = i + addValue
            
            if i > 9:
                addValue = i - 9
                i = i - 10
            else:
                addValue = 0
                
            rList = [i] + rList
        
        if addValue != 0:
            rList = [addValue] + rList
        
        
        return rList
