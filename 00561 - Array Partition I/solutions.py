class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        numsLen = len(nums)
        
        sum = 0

        while numsLen > 0:
            sum = sum + min(nums[numsLen - 1], nums[numsLen - 2])
            
            numsLen -= 2
            
        return sum
        
