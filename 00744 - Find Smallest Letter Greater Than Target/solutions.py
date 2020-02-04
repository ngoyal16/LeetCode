class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        
        if letters[-1] <= target:
            return letters[0]
        
        for char in letters:
            if char > target:
                return char
