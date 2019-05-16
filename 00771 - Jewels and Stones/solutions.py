class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        stones = {}
        
        for char in S:
            if char in stones:
                stones[char] = stones[char] + 1
            else:
                stones[char] = 1
                
        count = 0
        for char in J:
            if char in stones:
                count = count + stones[char]
            
        return count
