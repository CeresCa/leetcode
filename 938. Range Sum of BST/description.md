## 题目描述

> Given the root node of a binary search tree, return the sum of values of all nodes > with value between L and R (inclusive).
> The binary search tree is guaranteed to have unique values.
> 
> Example 1:
> 
> Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
> Output: 32
> Example 2:
> 
> Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
> Output: 23
> 
> Note:
> he number of nodes in the tree is at most 10000.
> The final answer is guaranteed to be less than 2^31.

## 解法说明
简单考察BST性质
> 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
> 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
> 任意节点的左、右子树也分别为二叉查找树；
> 没有键值相等的节点。

```python
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        ans = 0 
        if root:
            if L <= root.val <= R:
                ans += root.val
            if L < root.val:
                ans += self.rangeSumBST(root.left, L, R)
            if root.val < R:
                ans += self.rangeSumBST(root.right, L, R)
        return ans
```

如果根结点存在，且 L <= 根的值 <= R，则累加根的值；
如果L <= 根的值，说明L可以在左子树中查找，左子树作为新的根节点；
如果根的值 < R，说明L可以在右子树中查找，右子树作为新的根节点；