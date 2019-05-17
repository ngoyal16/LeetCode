class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        length = len(nums)
        
        if length == 0:
            # return 0 #nums[0]
            return "Line 7: IndexError: list index out of range"
        
        for i in range(length):
            if (nums[i] == target) or (nums[i] > target):
                    return i
                
        return length
