# hot100-lc 148. 排序链表

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.merge_sort(head)

    def merge_sort(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        left_head = head
        right_head = slow.next
        slow.next = None
        left = self.merge_sort(left_head)
        right = self.merge_sort(right_head)
        return self.merge(left, right)

    def merge(self, left, right):
        dummy_head = ListNode(-1)
        cur = dummy_head
        while left and right:
            if left.val <= right.val:
                cur.next = left
                cur = cur.next
                left = left.next
            else:
                cur.next = right
                cur = cur.next
                right = right.next

        while left:
            cur.next = left
            cur = cur.next
            left = left.next

        while right:
            cur.next = right
            cur = cur.next
            right = right.next

        return dummy_head.next
