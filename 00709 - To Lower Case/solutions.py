class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ''
        for ch in str:
            ascVal = ord(ch)
            if ascVal >= 65 and ascVal <= 90:
                res = res + chr(ascVal + 32)
            else:
                res = res + ch
        return res 
        
