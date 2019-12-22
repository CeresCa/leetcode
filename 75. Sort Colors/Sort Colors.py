class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if A == []:
            return
        length = len(A)
        p0 = 0
        p2 = length - 1
        i = 0
        while i <= p2:
            if A[i] == 2:
                A[p2], A[i] = A[i], A[p2]
                p2 -= 1
            elif A[i] == 0:
                A[p0], A[i] = A[i], A[p0]
                p0 += 1
                i += 1
            else:
                i += 1
