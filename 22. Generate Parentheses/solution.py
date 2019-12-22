class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(s='', left=0, right=0):
            """回溯法解决树形结构的暴力遍历问题"""
            if len(s) == 2 * n:  # 终止条件
                ans.append(s)
                return
            else:
                if left < n: # 左括号数不到一半，持续添加左括号
                    backtrack(s+'(', left+1, right)
                if right < left:  # 当右括号数小于左括号数，持续添加右括号
                    backtrack(s+')', left, right + 1)
        backtrack()
        return ans