class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        
        for idx, num in enumerate(nums):
            if num in temp:
                return [temp[num], idx]
            
            temp[target - num] = idx
