# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        current = result = ListNode(0)
        while l1 or l2 or carry:  # 当两个链表有没遍历完或者还有余数
            current.val = carry
            if l1:
                current.val += l1.val
                l1 = l1.next
            if l2:
                current.val += l2.val
                l2 = l2.next
            carry = current.val // 10
            current.val = current.val % 10  # 余数变成当前和整除10，节点值为和mod 10
            if l1 or l2 or carry:  # 当两个链表有没遍历完或者还有余数，继续创建新节点
                current.next = ListNode(0)
                current = current.next
        return result

