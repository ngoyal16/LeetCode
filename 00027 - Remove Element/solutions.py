class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        orignalLength = len(nums)
        
        if orignalLength == 0:
            return 0
        
        if orignalLength == 1 and nums[0] == val:
            return 0
            
        # orignalLength = orignalLength - 1
        i = 0
        
        while i < orignalLength:
            if val == nums[orignalLength - 1]:
                orignalLength = orignalLength - 1
                continue
                
            if val == nums[i]:
                nums[i] = nums[orignalLength - 1]
                nums[orignalLength - 1] = val
                orignalLength = orignalLength - 1
            
            i = i + 1
        
        return orignalLength
