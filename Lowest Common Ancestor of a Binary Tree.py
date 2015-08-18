# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}

    def lowestCommonAncestor(self, root, p, q):
        # 如果当前节点为空或者与目标节点之一相同，则返回当前节点
        # 递归寻找p和q在左右子树中的位置
        # 如果p和q分别位于root的左右两侧，则root为它们的LCA，否则为左子树或者右子树

        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(self, root.left, p, q)
        right = self.lowestCommonAncestor(self, root.right, p, q)
        return root if left and right else left or right
