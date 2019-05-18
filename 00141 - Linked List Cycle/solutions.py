# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
          return False
        
        l = head.next
        
        while head != l:
          if l is None or l.next is None:
            return False
          
          head = head.next
          l = l.next.next
        
        return True
