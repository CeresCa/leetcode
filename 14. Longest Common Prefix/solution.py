class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        '''有多种解法：水平扫描、垂直扫描、分治、二分查找等'''
        res = ""
        if strs == []:
            return ""
        if strs == [""]:
            return ""
        for i in range(min([len(i) for i in strs])):
            temp = strs[0][i]
            for j in strs:
                if j[i] != temp:
                    return res
            res += temp
        return res
