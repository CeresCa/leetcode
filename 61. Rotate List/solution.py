# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head
        
        dummy = ListNode(None)
        dummy.next = head
        slow = fast = dummy
        
        size = 0
        while fast.next:
            size += 1
            fast = fast.next
        
        for pos in range(size - k % size, 0, -1):
            slow = slow.next
            
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None

        return dummy.next