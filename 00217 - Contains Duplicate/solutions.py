class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        rDict = {}
        
        for num in nums:
            if rDict.has_key(num):
                return True
            
            rDict[num] = num
            
        return False
