# hot100-lc 23. 合并K个升序链表

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        """
        归并排序秒杀:
        先写两个有序链表的合并, 再递归分治
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, node1, node2):
        head = ListNode(0)
        cur = head
        while node1 and node2:
            if node1.val < node2.val:
                cur.next = node1
                node1 = node1.next
            else:
                cur.next = node2
                node2 = node2.next
            cur = cur.next

        while node1:
            cur.next = node1
            cur = cur.next
            node1 = node1.next

        while node2:
            cur.next = node2
            cur = cur.next
            node2 = node2.next
        return head.next

