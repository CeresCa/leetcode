/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    carry := 0
    current := &ListNode{0,nil}
    result := current
    for l1 != nil || l2 != nil || carry != 0 {
        current.Val = carry
        if l1 != nil {
            current.Val += l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            current.Val += l2.Val
            l2 = l2.Next
        }
        carry = current.Val / 10
        current.Val = current.Val % 10
        if l1 != nil || l2 != nil || carry != 0 {
            current.Next = &ListNode{0,nil}
            current = current.Next
        }
        }
    return result
}