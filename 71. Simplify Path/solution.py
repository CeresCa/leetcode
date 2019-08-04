class Solution:
    def simplifyPath(self, path: str) -> str:
        # 去除点号和空字符串
        path_list = [p for p in path.split("/") if p not in ("", ".")]
        stack = []
        for p in path_list:
            # 不是两点时一直入栈，遇到两点切栈不为空时出栈
            if p != "..":
                stack.append(p)
            elif len(stack) > 0 and p == "..":
                stack.pop()

        return "/" + "/".join(stack)

