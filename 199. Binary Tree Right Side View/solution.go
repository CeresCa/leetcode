/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */


 func rightSideView(root *TreeNode) []int {
    if root == nil {
        return []int{}
    }
    que := []*TreeNode{root}
    res := []int{}
    for len(que) != 0 {
        res = append(res, que[len(que)-1].Val)
        
        length := len(que)
        for i := 0; i < length; i++ {
            node := que[0]
            que = que[1:]
            if node.Left != nil {
                que = append(que, node.Left)

            }
            if node.Right != nil {
                que = append(que, node.Right)
            }
        
        }

    }
    return res
}