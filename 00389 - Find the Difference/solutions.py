class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        res = {}
        
        for ch in s:
            if ch in res:
                res[ch] = res[ch] + 1
            else:
                res[ch] = 1
                
        for ch in t:
            if ch in res:
                res[ch] = res[ch] - 1
                
                if res[ch] == 0:
                    del res[ch]
            else:
                return ch
