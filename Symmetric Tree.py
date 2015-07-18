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
        else:
            return self.isMirrror(root.left, root.right)

    def isMirrror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        else:
            return self.isMirrror(left.left, right.right) and self.isMirrror(left.right, right.left)
