class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lst=nums1+nums2
        lst.sort()
        
        n = len(lst)
        if n < 1:
            return None
        if n % 2 == 1:
            return (lst)[n//2]
        else:
            return sum((lst)[n//2-1:n//2+1])/2.0
