class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        length = len(S)
        i = 0
        
        res = []
        
        for ch in S:
            if ch == "I":
                res.append(i)
                i += 1
            else:
                res.append(length)
                length -= 1
        
        res.append(i)
        return res
