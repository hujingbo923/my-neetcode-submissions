class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []

        def dfs(first):

            if first == len(nums):
                ans.append(path[:])
                # path = []
                return
            path.append(nums[first])
            dfs(first + 1)
            temp = path.pop()
            while first + 1 < len(nums) and temp == nums[first + 1]:
                first += 1
            dfs(first + 1)

        dfs(0)
        return ans
