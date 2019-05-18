# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
    def deleteDuplicates(self, head, currVal = None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
          return head
        
        if head.val == currVal:
          return self.deleteDuplicates(head.next, head.val)
          
        l = ListNode(head.val)
        l.next = self.deleteDuplicates(head.next, head.val)
        
        return l
