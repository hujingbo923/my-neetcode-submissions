# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:#如果是1，2，none，这里会报错，要加一个fast.next
            if slow ==fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False