class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        seen = {}
        for i in range(l):
            seen[nums[i]] = seen.get(nums[i], 0) + 1
            if seen[nums[i]] == 2:
                return True
        return False