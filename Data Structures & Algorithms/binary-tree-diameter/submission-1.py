# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node == None:
                return 0
            ans1 = dfs(node.left)
            ans2 = dfs(node.right)
            self.ans = max(self.ans, ans1 + ans2)
            return 1 + max(ans1, ans2)
        dfs(root)
        return self.ans