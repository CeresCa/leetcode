class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        return (
            self.findKth(nums1, nums2, l // 2)
            if l % 2 == 1
            else (
                self.findKth(nums1, nums2, l // 2 - 1)
                + self.findKth(nums1, nums2, l // 2)
            )
            / 2.0
        )

    def findKth(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k]
        if len(nums2) == 0:
            return nums1[k]
        index1, index2 = len(nums1) // 2, len(nums2) // 2
        median1, median2 = nums1[index1], nums2[index2]
        # nums，nums2以中间位置分为四部分，
        # 如果 (m/2 + n/2) > k，那么意味着，当前中位数取高了，正确的中位数要么在 Section 1或者Section3中。
        # 如果nums1[m/2] > nums2[n/2], 意味着中位数肯定不可能在Section 2里面，那么新的搜索可以丢弃这个区间段了。
        # 同理可以推断出余下三种情况

        if median1 < median2:
            if (index1 + index2) >= k:
                return self.findKth(nums1, nums2[:index2], k)
            else:
                return self.findKth(nums1[index1 + 1 :], nums2, k - index1 - 1)
        else:
            if (index1 + index2) >= k:
                return self.findKth(nums1[:index1], nums2, k)
            else:
                return self.findKth(nums1, nums2[index2 + 1 :], k - index2 - 1)
