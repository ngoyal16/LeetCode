class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        res = []
        
        for i in range(numRows):
            temp = []
            temp.append(1)
            
            if i > 0:
                prevRow = res[i - 1]
                prevLen = len(prevRow)
                
                for j in range(prevLen - 1):
                    temp.append(prevRow[j] + prevRow[j + 1])
                
                temp.append(1)
            
            res.append(temp)
            
        return res
