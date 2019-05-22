class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dic = {}
        
        for num in nums:
          if num in dic:
            dic[num] += 1
          else:
            dic[num] = 1
        
        minVal = (len(nums) / 2) + 1
        
        for key in dic:
          if minVal <= dic[key]:
            return key
