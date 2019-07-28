class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a_list = A.split(" ")
        b_list = B.split(" ")
        a_dict = dict()
        b_dict = dict()
        for a in a_list:
            if a not in a_dict:
                a_dict[a] = 1
            else:
                a_dict[a] += 1

        for b in b_list:
            if b not in b_dict:
                b_dict[b] = 1
            else:
                b_dict[b] += 1

        res = []
        for a in a_list:
            if a not in b_dict and a_dict[a] == 1:
                res.append(a)

        for b in b_list:
            if b not in a_dict and b_dict[b] == 1:
                res.append(b)
        return res
