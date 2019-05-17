class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        arr = s.split()
        
        if len(arr) == 0:
            return 0
        
        w = arr[-1]
        return len(w)
