class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        stack = -1
        res = ""
        
        for ch in S:
            if ch == "(":
                stack += 1
                
            if stack >= 1:
                res += ch
                
            if ch == ")":
                stack -= 1
                
        return res
