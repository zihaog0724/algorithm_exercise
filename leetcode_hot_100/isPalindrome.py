# hot100-lc 234. 回文链表

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = self.reverse(slow.next)
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def reverse(self, head):
        cur = head
        pre = None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre
