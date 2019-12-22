class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        nums3 = self.merge(nums1, nums2)

        return (
            nums3[total // 2]
            if total % 2
            else (nums3[total // 2 - 1] + nums3[total // 2]) / 2
        )

    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """merge two sorted array"""
        size1 = len(nums1)
        size2 = len(nums2)
        result = []
        index1 = index2 = 0
        while index1 != size1 and index2 != size2:
            if nums1[index1] < nums2[index2]:
                result.append(nums1[index1])
                index1 += 1
            else:
                result.append(nums2[index2])
                index2 += 1
        result += nums1[index1:]
        result += nums2[index2:]
        return result
