# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if root is None:
            return True
        stack = []
        stack.append((root.left, root.right))
        while stack:
            left, right = stack.pop(0)
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            else:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
        return True
