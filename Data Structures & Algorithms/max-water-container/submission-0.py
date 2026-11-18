class Solution:
    def maxArea(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        ans = 0
        while left < right:
            height = min(nums[left], nums[right])
            width = right - left
            ans = max(ans, height * width)
            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1

        return ans