"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
          return 0
        
        if len(root.children):
          return 1 + max(map(self.maxDepth, root.children))
        else:
          return 1
