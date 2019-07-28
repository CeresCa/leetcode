/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func inorder(node *TreeNode, nodes []int) []int {
    if node != nil {
        nodes = inorder(node.Left, nodes)
        nodes = append(nodes, node.Val)
        nodes = inorder(node.Right, nodes)
    }
    return nodes
}

func increasingBST(root *TreeNode) *TreeNode {
    nodes := []int{}
    nodes = inorder(root,nodes)
    cur := &TreeNode{nodes[0], nil, nil}
    ans := cur
    for _,n := range nodes[1:] {
        cur.Right = &TreeNode{n, nil, nil}
        cur = cur.Right
    }
    return ans
    
}