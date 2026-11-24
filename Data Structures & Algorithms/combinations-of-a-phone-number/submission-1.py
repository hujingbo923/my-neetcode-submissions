class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        map1 = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        path = []
        ans = []

        def dfs(i):
            if i == len(digits):
                ans.append("".join(path))
                return
            for j in map1[digits[i]]:
                path.append(j)
                dfs(i + 1)
                path.pop()

        dfs(0)
        return ans
