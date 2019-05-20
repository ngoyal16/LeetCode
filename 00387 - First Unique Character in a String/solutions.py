class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = {}
        
        for ch in s:
            if ch in res:
                res[ch] = res[ch] + 1
            else:
                res[ch] = 1
                
        rtValue = -1
        
        for ch in s:
            if res[ch] == 1:
                return s.index(ch)
        
        return rtValue
