class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        
        for i in range(rowIndex + 1):
            temp = []
            temp.append(1)
            
            if i > 0:
                # res = res[i - 1]
                prevLen = len(res)
                
                for j in range(prevLen - 1):
                    temp.append(res[j] + res[j + 1])
                
                temp.append(1)
            
            res = temp
            
        return res
