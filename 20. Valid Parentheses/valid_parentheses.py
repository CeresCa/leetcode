class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        queue = []
        par = {')': '(',
               ']': '[',
               '}': '{'}

        for c in s:
            if c in list(par.values()):
                queue.append(c)
            elif c in list(par.keys()):
                if not queue:
                    return False
                result = queue.pop()
                if result != par[c]:
                    return False
        if queue:
            return False
        else:
            return True
