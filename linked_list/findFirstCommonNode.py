'''
输入两个链表，找出它们的第一个公共结点。
'''

# 
# @param pHead1 ListNode类 
# @param pHead2 ListNode类 
# @return ListNode类
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None

        cur1 = pHead1
        cur2 = pHead2
        while cur1 != cur2:
            cur1 = cur1.next if cur1 else pHead2 # 必须用cur1判断节点是否为空，不能用cur1.next，否则若两链表无节点则进入死循环
            cur2 = cur2.next if cur2 else pHead1 # 必须用cur2判断节点是否为空，不能用cur2.next，否则若两链表无节点则进入死循环
        return cur1

#Test
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

l2 = ListNode(6)
l2.next = ListNode(4)
l2.next.next = l1.next
#l2.next.next = ListNode(2)

solution = Solution()
print(solution.FindFirstCommonNode(l1,l2))
