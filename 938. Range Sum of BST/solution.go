package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rangeSumBST(root *TreeNode, L int, R int) int {
	ans := 0
	if root != nil {
		if L <= root.Val && root.Val <= R {
			ans += root.Val
		}
		if root.Val > L {
			ans += rangeSumBST(root.Left, L, R)
		}
		if root.Val < R {
			ans += rangeSumBST(root.Right, L, R)
		}
	}
	return ans
}

func main() {
	left := TreeNode{3, nil, nil}
	right := TreeNode{7, nil, nil}
	root := TreeNode{5, &left, &right}
	fmt.Println(rangeSumBST(&root, 1, 3))
}
