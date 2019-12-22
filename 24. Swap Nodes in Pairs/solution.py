# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = pair = ListNode(0)  # dummy:伪首, pair: 每个节点对之前的节点
        dummy.next = head
        while head and head.next:
            tmp_next = head.next  # 要交换节点当时的后一个节点
            head.next = tmp_next.next  # 当时的下下个
            tmp_next.next = head  # 当时的后一个的next指向当前节点
            pair.next = tmp_next  # 每对节点之前的节点的next 指向新节点对的第一个
            head = head.next  # 当前节点变成原始链表的下下个
            pair = tmp_next.next  # 跳到下一对未调整的节点对之前
        return dummy.next
