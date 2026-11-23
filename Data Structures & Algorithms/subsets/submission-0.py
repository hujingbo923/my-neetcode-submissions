class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def dfs(first):
            if first == len(nums):
                ans.append(path[:])
                # path = []
                return
            path.append(nums[first])
            dfs(first + 1)
            path.pop()
            dfs(first + 1)

        dfs(0)
        return ans