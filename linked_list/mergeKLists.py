# leetcode 23. mergeKLists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l, r):
        # l, r = lists[0], lists[1]
        dummyHead = ListNode(0)
        cur = dummyHead
        while l and r:
            if l.val <= r.val:
                cur.next = l
                cur = cur.next
                l = l.next
            else:
                cur.next = r
                cur = cur.next
                r = r.next
        while l:
            cur.next = l
            cur = cur.next
            l = l.next
        while r:
            cur.next = r
            cur = cur.next
            r = r.next
        return dummyHead.next
