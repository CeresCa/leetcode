class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        stack = deque()
        par = {')': '(',
               ']': '[',
               '}': '{'}
        values = par.values()
        keys = par.keys()

        for c in s:
            if c in values:
                stack.append(c)
            elif c in keys:
                if not stack:
                    return False
                result = stack.pop()
                if result != par[c]:
                    return False
        if stack:
            return False
        else:
            return True
