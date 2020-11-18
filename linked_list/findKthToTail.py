'''
输入一个链表，输出该链表中倒数第k个结点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head:
            return None

        slow = head
        fast = head
        for i in range(k):
            if not fast:
                return None
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        return slow


#Test
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

solution = Solution()
print(solution.FindKthToTail(l1, 6).val)
