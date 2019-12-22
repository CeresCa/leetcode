# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """先后指针法，另一种解法：先遍历求出链表长度"""
        if head.next is None:
            return None

        fast = head
        slow = head
        for step in range(0, n):
            fast = fast.next
        if not fast:
            # 头节点为待删除节点
            head = head.next
            return head
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        if slow.next:
            slow.next = slow.next.next
        return head
