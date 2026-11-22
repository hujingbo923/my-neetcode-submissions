"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        search = set()
        while p:
            search.add(p)
            p = p.parent
        while q not in search:
            search.add(q)
            q = q.parent
        return q