class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []

        def dfs(left, right):
            if left == n and right == n:
                ans.append("".join(stack))
                return
            if left < n:
                stack.append("(")
                dfs(left + 1, right)
                stack.pop()
            if left > right:
                stack.append(")")
                dfs(left, right + 1)
                stack.pop()

        dfs(0, 0)
        return ans
