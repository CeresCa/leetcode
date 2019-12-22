/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    if l1 == nil{
        return l2
    }
    if l2 == nil{
        return l1
    }
    curr := &ListNode{0, nil}
    head := curr
    for l1 != nil && l2 != nil{
        if l2.Val < l1.Val{
            curr.Next = l2
            l2 = l2.Next
        } else {
            curr.Next = l1
            l1 = l1.Next 
        }
        curr = curr.Next
    if l1 != nil{
        curr.Next = l1
    } else if l2 != nil{
        curr.Next = l2
    }
    }
    return head.Next
}