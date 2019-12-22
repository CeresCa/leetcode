# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if p == q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Short version:
# def isSameTree(self, p, q):
#   if p and q:
#        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#   else:
#       return p == q
