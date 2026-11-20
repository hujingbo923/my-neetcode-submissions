# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root == None:
            return depth
        depth = self.maxDepth(root.left) + 1
        depth = max(depth, self.maxDepth(root.right) + 1)
        return depth

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if root == None:
            return ans
        ans0 = self.maxDepth(root.left) + self.maxDepth(root.right)
        ans1 = self.diameterOfBinaryTree(root.left)
        ans2 = self.diameterOfBinaryTree(root.right)
        ans = max(ans0, ans1, ans2)
        return ans
