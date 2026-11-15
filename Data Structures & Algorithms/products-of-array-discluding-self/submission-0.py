class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all1 = 1
        count = 0
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                all1 *= nums[i]
        for i in range(len(nums)):
            if count == 0:
                ans[i] = all1 // nums[i]
            else:
                if nums[i] == 0 and count == 1:
                    ans[i] = all1
                else:
                    ans[i] = 0
        return ans