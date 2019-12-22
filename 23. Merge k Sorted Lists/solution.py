# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            size = len(lists)
            interval = 1
            while interval < size:
                for i in range(0, size - interval, interval * 2):
                    lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
                interval *= 2
            return lists[0]

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            merge_head = curr = ListNode(0)

            while l1 and l2:
                if l1.val > l2.val:
                    curr.next = l2
                    l2 = l2.next
                else:
                    curr.next = l1
                    l1 = l1.next
                curr = curr.next

                curr.next = l1 or l2
            return merge_head.next
