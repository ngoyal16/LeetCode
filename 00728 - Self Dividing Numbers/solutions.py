class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        res = []
        for num in range(left, right+1):
            x = str(num)
            
            if '0' not in x:
                if self.checkDivisibility(num):
                    res.append(num)
        
        return res
    
    def checkDivisibility(self, num):
        
        temp = num
        
        while temp > 0:
            if num % (temp % 10) != 0:
                return False
            
            temp = temp / 10
            
        return True
