class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        i = 0
        nLen = len(needle)
        sLen = len(haystack) - nLen
        while(i <= sLen):
            if (haystack[i:i+nLen] == needle):
                return i
            i = i+1
            
        return -1
        
