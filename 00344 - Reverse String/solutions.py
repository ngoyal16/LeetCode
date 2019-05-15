class Solution(object):
    def reverseString(self, s, left=0, right=None):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if right is None:
            right = len(s) - 1
            
        
        if left >= right:
            return s
        
        
        s[left], s[right] = s[right], s[left]
        
        return self.reverseString(s, left+1, right-1)
