class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        length = len(height)
        left = 0 
        right = length - 1
        lmax = 0
        rmax = 0
        ans = 0
        while left < right:
                if height[left] > lmax:
                    lmax = height[left]
                if height[right] > rmax:
                    rmax = height[right]
                if lmax < rmax:
                    ans += max(0, lmax - height[left])
                    left += 1

                else:
                    ans += max(0, rmax - height[right])
                    right -= 1
        return ans