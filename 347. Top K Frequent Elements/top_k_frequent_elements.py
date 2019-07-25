class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        bucket = [0] * (abs(max(nums)) + abs(min(nums)) + 1)
        for n in nums:
            bucket[n] += 1
        res = []
        for i, v in enumerate(bucket, min(min(nums),0)):
            if v > 0:
              res.append(i)
        return res[:k]


