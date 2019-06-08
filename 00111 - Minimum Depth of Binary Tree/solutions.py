# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        
        lDepth = self.minDepth(root.left)
        rDepth = self.minDepth(root.right)
        
        if lDepth != 0 and rDepth != 0:
            return 1 + min(lDepth, rDepth)
        
        if lDepth == 0:
            return 1 + rDepth
        
        if rDepth == 0:
            return 1 + lDepth
        
