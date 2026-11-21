# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        ans = []
        if root == None:
            return ans
        while q:
            n = len(q)
            for i in range(n):
                temp = q.popleft()
                if temp.left != None:
                    q.append(temp.left)
                if temp.right != None:
                    q.append(temp.right)
                if i == n - 1:
                    ans.append(temp.val)
        return ans
