# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root, rootVal = None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            return True
        
        if rootVal is not None:
            return root.val == rootVal and self.isUnivalTree(root.left, root.val) and self.isUnivalTree(root.right, root.val)
        
        return self.isUnivalTree(root.left, root.val) and self.isUnivalTree(root.right, root.val)
