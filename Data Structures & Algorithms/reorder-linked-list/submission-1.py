# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1 2 3 4 5
# 1 2 3 4 5 6
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = []
        cur = head
        while cur:
            node.append(cur)
            cur = cur.next
        l = 0
        r = len(node) - 1
        while l < r:
            node[l].next = node[r]
            l += 1
            if l >= r:
                node[r].next = None
                break
            node[r].next = node[l]
            r -= 1
        node[l].next = None