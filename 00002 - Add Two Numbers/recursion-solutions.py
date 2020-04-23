# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        sum = l1.val + l2.val + carry
        carry = 0
        
        if sum > 9:
            carry = int(sum / 10)
            sum = int(sum - (carry * 10))
        
        l3 = ListNode(sum)
        
        if l1.next is not None and l2.next is not None:
            l3.next = self.addTwoNumbers(l1.next, l2.next, carry)
        elif l1.next is None and l2.next is not None:
            l3.next = self.addTwoNumbers(ListNode(carry), l2.next, 0)
        elif l1.next is not None and l2.next is None:
            l3.next = self.addTwoNumbers(l1.next, ListNode(carry), 0)
        elif l1.next is None and l2.next is None:
            if carry != 0:
                l3.next = ListNode(carry)
          
        return l3
