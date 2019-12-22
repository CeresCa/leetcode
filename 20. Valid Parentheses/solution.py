class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque

        stack = deque()
        par = {")": "(", "]": "[", "}": "{"}
        left = par.values()
        right = par.keys()

        for c in s:
            if c in left:
                stack.append(c)
            elif c in right:
                if not stack:
                    return False
                result = stack.pop()
                if result != par[c]:
                    return False
        if stack:
            return False
        else:
            return True
