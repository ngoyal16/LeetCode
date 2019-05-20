class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        num = nums.pop()
        
        while True:
            try:
                nums.remove(num)
            except:
                return num
            
            num = nums.pop()
