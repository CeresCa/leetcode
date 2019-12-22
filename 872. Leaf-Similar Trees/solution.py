# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import Generator


class Solution:
    """遍历到叶子节点，添加值到列表中，或者用生成器"""

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return list(self.get_leaves(root1)) == list(self.get_leaves(root2))

    def get_leaves(self, root: TreeNode) -> Generator[int, None, None]:
        if not root.left and not root.right:
            yield root.val

        if root.left:
            yield from self.get_leaves(root.left)

        if root.right:
            yield from self.get_leaves(root.right)
