# hot100-lc 19. 删除链表的倒数第N个结点

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """
        快慢指针法找到倒数第n个节点的前一个slow, 然后slow.next = slow.next.next
        一个细节: 如果倒数第n个节点的n等于链表长度, 那么直接需要特殊处理, 直接返回head.next即可
        """
        if not head:
            return None

        fast = head
        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
