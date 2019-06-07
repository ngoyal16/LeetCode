class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        sortedHeights = sorted(heights)
        
        return sum(map(lambda x,y : 0 if x == y else 1, heights, sortedHeights))
