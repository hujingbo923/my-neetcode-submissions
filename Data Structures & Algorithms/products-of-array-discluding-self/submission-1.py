class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        qian = [0] * len(nums)
        hou = [0] * len(nums)
        ans = [0] * len(nums)
        qian[0] = 1
        hou[-1] = 1
        for i in range(1, len(nums)):
            qian[i] = nums[i-1] * qian[i-1]
        for i in range(len(nums)-2, -1, -1):
            hou[i] = hou[i+1] * nums[i+1]
        for i in range(len(nums)):
            ans[i] = qian[i] * hou[i]
        return ans