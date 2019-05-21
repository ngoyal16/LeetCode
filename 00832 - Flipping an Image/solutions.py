class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        res = []
        
        for items in A:
            temp = []
            for item in reversed(items):
                temp.append(int(not item))
                            
            res.append(temp)
                            
        return res
