# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if node == None:
                return [True, 0]
            if (
                dfs(node.left)[0] == True
                and dfs(node.right)[0] == True
                and abs(dfs(node.left)[1] - dfs(node.right)[1]) <= 1
            ):
                return [True, 1 + max(dfs(node.left)[1], dfs(node.right)[1])]  # dfs记得加1
            else:
                return [False, 1 + max(dfs(node.left)[1], dfs(node.right)[1])]

        return dfs(root)[0]
