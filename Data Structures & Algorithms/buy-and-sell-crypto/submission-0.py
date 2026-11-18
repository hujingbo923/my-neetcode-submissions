class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        stack = []
        stack.append(nums[0])
        ans = 0
        for i in nums:
            if i <stack[0]:
                stack[0] = i
            else:
                ans = max(ans, i - stack[0])
        return ans