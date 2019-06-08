# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        length = len(nums)
        if length == 0:
            return None
        
        if length == 1:
            return TreeNode(nums[0])
        
        idx = ((length+1) / 2) if (length%2 == 1) else ((length / 2) + 1)
        
        tNode = TreeNode(nums[idx - 1])
        tNode.left = self.sortedArrayToBST(nums[:idx - 1])
        tNode.right = self.sortedArrayToBST(nums[idx:])
        
        return tNode
