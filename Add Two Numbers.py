# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        current = result = ListNode(0)
        while l1 or l2 or carry:
            current.val = carry
            if l1:
                current.val += l1.val
                l1 = l1.next
            if l2:
                current.val += l2.val
                l2 = l2.next
            carry = current.val // 10
            current.val = current.val % 10
            if l1 or l2 or carry:
                current.next = ListNode(0)
                current = current.next
        return result
