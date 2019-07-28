# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """将BST转为全右子树结构，先序遍历获得值列表，再重建"""

    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def inorder(node, nodes):
            if node:
                inorder(node.left, nodes)
                nodes.append(node.val)
                inorder(node.right, nodes)

        inorder(root, nodes)

        ans = cur = TreeNode(nodes[0])
        for n in nodes[1:]:
            cur.right = TreeNode(n)
            cur = cur.right

        return ans
