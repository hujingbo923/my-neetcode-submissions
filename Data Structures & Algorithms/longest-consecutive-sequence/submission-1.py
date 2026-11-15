class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set()
        cnt = 0
        ans = 0
        for i in range(len(nums)):
            hash.add(nums[i])
        for i in nums:
            if i - 1 not in hash:
                flag = i
                cnt = 0
                while flag in hash:
                    cnt += 1
                    flag += 1
                ans = max(ans, cnt)
                continue
        return ans