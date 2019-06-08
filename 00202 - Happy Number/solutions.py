class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        res = sum([int(i)**2 for i in list(str(n))])
        
        temp = []

        while (True):
            if (res == 1):
                return True

            if (res == n or res in temp):
                return False
            
            temp.append(res)
            res = sum([int(i)**2 for i in list(str(res))])
