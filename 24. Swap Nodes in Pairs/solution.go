/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

 func swapPairs(head *ListNode) *ListNode {
    pair :=  &ListNode{0, nil}
    dummy := pair
    dummy.Next = head
    for head != nil && head.Next != nil {
        tmp_next := head.Next
        head.Next = tmp_next.Next
        tmp_next.Next = head
        pair.Next =  tmp_next
        head = head.Next
        pair = tmp_next.Next
    }
    return dummy.Next
}