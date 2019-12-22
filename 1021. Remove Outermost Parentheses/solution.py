class Solution:
    """
    opened变量统计尚未闭合的左括号数量，result当作栈，当括号不在最外层时入栈
    """

    def removeOuterParentheses(self, S: str) -> str:
        result = []
        opened = 0
        for c in S:
            if c == "(" and opened > 0:
                result.append(c)
            elif c == ")" and opened > 1:
                result.append(c)
            if c == "(":
                opened += 1
            else:
                opened -= 1
        return "".join(result)
