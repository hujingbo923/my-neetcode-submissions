class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        max1 = r  # 这里因为整除是向下取整，所以l如果不变的话，就会死循环
        if nums[max1] <= target <= nums[-1]:
            l, r = max1, len(nums) - 1
        else:
            l, r = 0, max1 - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1
