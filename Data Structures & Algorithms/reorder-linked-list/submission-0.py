class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next  # 先反转链表
        slow.next = None
        pre = None
        while second:
            temp = second.next
            second.next = pre
            pre = second
            second = temp

        # 这里second已经是none，而不是前置节点
        while pre and head:
            temp1 = head.next
            head.next = pre
            pre = pre.next
            head.next.next = temp1  # 这里pre已经变了，不能再用pre
            head = temp1
        # 要看清楚后面用的节点会不会变化，如果会变化需要提前更新
