# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        while root:  # 不需要提前判空，交给下一轮判空
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:  # 如果648这样，必须else退出，就直接排除都在左边或者都在右边的情况
                return root
        # 如果左右左右左，这个方法就不对了，因为只能一股脑左拐，然后一股脑右拐
        # while p.val < root.val and q.val < root.val:
        #    root = root.left
        # while p.val > root.val and q.val > root.val:
        #    root = root.right
        # return root
