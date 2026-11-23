# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        now = head
        prep = None
        last = now.next
        while now!=None:
            last = now.next
            now.next =prep
            prep = now
            now = last
        return prep #这里如果返回now就是返回none了