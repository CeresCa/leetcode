# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        que = []
        res = []
        que.append(root)
        while que:
            res.append(que[-1].val)
            length = len(que)
            for i in range(length):
                node = que.pop(0)
                if node:
                    if node.left is not None:
                        que.append(node.left)
                    if node.right is not None:
                        que.append(node.right)
        return res
