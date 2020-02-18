class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        
        idx = 0
        lenT = len(typed)
        lenN = len(name)
        
        for i in range(lenT):
            if idx < lenN and typed[i] == name[idx]:
                idx += 1
            elif i == 0 or typed[i] != typed[i-1]:
                return False
        return idx == lenN
