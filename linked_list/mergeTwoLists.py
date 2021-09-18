# 将两个有序的链表合并为一个新链表，要求新的链表是通过拼接两个链表的节点来生成的。

# 
# @param l1 ListNode类 
# @param l2 ListNode类 
# @return ListNode类
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self , l1 , l2 ):
        # write code here
        # 先判断两个链表为空的情况
        if not l1 and not l2:
            return None
        if not l1 and l2:
            return l2
        if l1 and not l2:
            return l1

        # 合并链表
        l = ListNode(0)
        head = l
        while l1 and l2:
            if l1.val <= l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next

        if l1:
            l.next = l1
        elif l2:
            l.next = l2
        return head.next


l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)
l1.next.next.next = ListNode(7)

l2 = ListNode(0)
l2.next = ListNode(4)
l2.next.next = ListNode(5)
l2.next.next.next = ListNode(8)

solution = Solution()
print(solution.mergeTwoLists(l1, l2).next.next.next.next.next.next.next.val)
