class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        
        if count < 2:
            return count
        
        i = 1
        j = 0
        while i < count:
            if (nums[j] != nums[i]):
                j = j+1
                nums[j] = nums[i]
            i = i+1
        return j+1
        
