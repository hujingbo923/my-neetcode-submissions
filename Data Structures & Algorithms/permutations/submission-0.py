class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        visited = [False] * len(nums)

        def dfs(path, nums, visited):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            else:
                for i in range(len(nums)):
                    if visited[i] == False:
                        visited[i] = True
                        path.append(nums[i])
                        dfs(path, nums, visited)
                        path.pop()
                        visited[i] = False
        dfs(path, nums, visited)

        return ans
