class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                m -= 1
                nums1[m + n] = nums1[m]
            else:
                n -= 1
                nums1[m + n] = nums2[n]
                
        
        if n > 0:
            nums1[:n] = nums2[:n]
