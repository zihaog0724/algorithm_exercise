'''
给定一个链表，删除链表的倒数第n个节点并返回链表的头指针
例如，
 给出的链表为:1->2->3->4->5, n= 2.
 删除了链表的倒数第n个节点之后,链表变为1->2->3->5.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        # write code here
        if not head:
            return None
        
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
            
        if not fast:
            return head.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
