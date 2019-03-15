class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        idx = 0
        large = nums[0]
        sLarge = 0
        
        n = len(nums)
        
        for i in range(1, n):
          if large < nums[i]:
            sLarge = large
            large = nums[i]
            idx = i
            
          else:
            if (sLarge <= nums[i]):
              sLarge = nums[i]
              
        if large < 2*sLarge:
          return -1
          
        return idx
        
