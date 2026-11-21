# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, low, high):
            if root == None:
                return True
            if root.val <= low:  # 这里还是，如果父大于左孩子，还得继续递归
                    return False
            if root.val >= high:
                    return False

            return dfs(root.right, root.val, high) and dfs(root.left, low, root.val)

        return dfs(root, float("-inf"), float("inf"))
