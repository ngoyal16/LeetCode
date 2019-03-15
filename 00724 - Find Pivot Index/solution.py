class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      lSum = 0
      rSum = 0
      n = len(nums)
      
      for num in nums:
        rSum = rSum + num
        
      for i in range(n):
        rSum = rSum - nums[i]
        
        if (lSum == rSum):
          return i
        
        lSum = lSum + nums[i]
        
      return -1
