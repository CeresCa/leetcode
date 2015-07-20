# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        res = []
        self.buildVector(root, 0, res)
        return res

    def buildVector(self, root, level, res):
        if root is None:
            return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        self.buildVector(root.left, level + 1, res)
        self.buildVector(root.right, level + 1, res)
