class Solution:
    def exist(self, nums: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(nums[0]))] for _ in range(len(nums))]

        def dfs(hang, lie, lenth):
            if lenth == len(word):
                return True
            if (
                hang < 0
                or lie < 0
                or hang >= len(nums)
                or lie >= len(nums[0])
                or nums[hang][lie] != word[lenth]
                or visited[hang][lie] == True
            ):
                return False
            else:
                visited[hang][lie] = True
            ans = (
                dfs(hang + 1, lie, lenth + 1)
                or dfs(hang - 1, lie, lenth + 1)
                or dfs(hang, lie + 1, lenth + 1)
                or dfs(hang, lie - 1, lenth + 1)
            )
            visited[hang][lie] = False
            return ans

        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if dfs(i, j, 0):
                    return True
        return False
