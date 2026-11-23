class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        sub = []

        def dfs(i):
            if sum(sub) == target:  # 先判断有没有答案，如果正好长度一致，这样就漏掉答案了
                ans.append(sub[:])
                return
            if i == len(nums):
                return
            if sum(sub) > target:
                return
            sub.append(nums[i])
            dfs(i)
            sub.pop()
            dfs(i + 1)

        dfs(0)
        return ans
