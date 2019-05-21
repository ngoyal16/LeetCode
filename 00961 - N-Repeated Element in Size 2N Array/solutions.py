class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # A.sort()
        
        c = set()
        for num in A:
            if num in c:
                return num
            c.add(num)
