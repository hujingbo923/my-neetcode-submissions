# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        cur = head
        before = None
        lenth = 0

        while cur:  # 不能直接len，需要while计数
            cur = cur.next
            lenth += 1

        # 如果lenth = n，直接while的话，就不会删除
        if lenth == n:
            return head.next

        cur = head
        while i < lenth - n:
            before = cur
            cur = cur.next
            i += 1
        before.next = cur.next
        return head
