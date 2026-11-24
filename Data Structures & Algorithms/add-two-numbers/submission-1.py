# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        # 虚拟头节点
        head = ans
        cur = l1
        cur2 = l2
        temp = 0
        jinwei = 0

        while cur != None or cur2 != None or jinwei != 0:  # 有进位的话需要再来一次
            val1 = cur.val if cur else 0
            val2 = cur2.val if cur2 else 0
            temp = val1 + val2 + jinwei  # 可能两个有一个是空指针，这里需要判断一下
            jinwei = 0
            if temp >= 10:
                jinwei = 1
                temp -= 10
            head.next = ListNode(temp)  # 链表初始化
            head = head.next
            if cur != None:  # 要判断是否为空，要不然报错
                cur = cur.next
            if cur2 != None:
                cur2 = cur2.next
        return ans.next
