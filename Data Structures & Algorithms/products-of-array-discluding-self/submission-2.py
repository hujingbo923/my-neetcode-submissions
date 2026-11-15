class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        ans[0] = 1
        ans[-1] = 1
        pro = 1 #定义辅助变量，要不然好像一个数组实现不了
        for i in range(1, len(nums)):
            ans[i] = pro * nums[i-1]
            pro *= nums[i-1]
        pro = 1
        for i in range(len(nums)-2, -1, -1):
            ans[i] = ans[i]*pro * nums[i+1]
            pro = pro * nums[i+1]
        return ans #左边所有乘积 * 右边所有乘积就等于除了自身的所有乘积，放在一个数组中维护