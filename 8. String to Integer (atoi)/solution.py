class Solution:
    def myAtoi(self, str: "str") -> "int":
        str = str.strip()
        str = re.findall("(^[\+\-0]*\d+)\D*", str)
        try:
            result = int("".join(str))
            return max(-(2 ** 31), min(result, 2 ** 31 - 1))
        except:
            return 0
