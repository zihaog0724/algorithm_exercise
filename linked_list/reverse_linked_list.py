class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead == None:
            return None
        elif pHead.next == None:
            return pHead

        pre = None
        cur = pHead
        nex = None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre

# Test
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
solution = Solution()
l = solution.ReverseList(l1)

print(l.val)
print(l.next.val)
print(l.next.next.val)
