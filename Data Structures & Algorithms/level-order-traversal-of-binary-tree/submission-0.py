# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        quene = collections.deque()
        ans = []
        quene.append(root)
        while quene:
            n = len(quene)
            temp1 = []
            for i in range(n):
                temp = quene.popleft()
                if temp != None:
                    temp1.append(temp.val)
                    quene.append(temp.left)
                    quene.append(temp.right)
            if temp1:
                ans.append(temp1)
        return ans
            
