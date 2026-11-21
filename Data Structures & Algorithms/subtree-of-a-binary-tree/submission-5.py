# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if (p != None and q != None) and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
            
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        if (root != None and subRoot != None) and (root.val == subRoot.val):
            if self.isSameTree(root, subRoot):
                return True
        if root.left != None:#这里如果root = root.left那么下面root.right就是左孩子的右孩子，就不对了
            return self.isSubtree(root.left, subRoot)
        if root.right != None:
            return self.isSubtree(root.right, subRoot)
        return False