class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s is None:
            return True
        
        stack = []
        openPar = ['(', '{', '[']
        closePar = [')', '}', ']']
        
        for char in s:
            if char in openPar:
                stack.append(char)

            elif char in closePar:
                try:
                    temp = stack.pop()

                    if (
                        (temp == "(" and char != ")")
                        or (temp == "{" and char != "}")
                        or (temp == "[" and char != "]")
                    ):
                        return False
                except:
                    return False
        
        if len(stack):
            return False
        
        return True
