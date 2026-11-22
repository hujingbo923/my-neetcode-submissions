# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {val: i for i, val in enumerate(inorder)}
        pre = 0

        def dfs(left, right):
            nonlocal pre
            if left > right:  # l==r的时候是叶子节点，所以要l>r的时候return
                return None
            index = hashmap[preorder[pre]]
            root = TreeNode(preorder[pre])
            pre += 1
            root.left = dfs(left, index - 1)
            root.right = dfs(index + 1, right)
            return root

        return dfs(0, len(preorder) - 1)
