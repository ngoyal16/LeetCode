class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        print(n)
        
        
        res = ""
        
        while n > 0:
          rem = n % 26
          
          if rem == 0:
            res = 'Z' + res
            n = (n / 26) - 1
          else:
            res = chr(64 + rem) + res
            n = n / 26
            
        return res
