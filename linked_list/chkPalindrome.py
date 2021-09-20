# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class PalindromeList:
    def chkPalindrome(self, A):
        # write code here
        if not A:
            return False

        if not A.next:
            return True

        if not A.next.next:
            if A.val == A.next.val:
                return True
            else:
                return False

        fast = A
        slow = A
        while fast.next:
            if fast.next.next:
                slow = slow.next
                fast = fast.next.next
            else:
                break
        
        # reverse right part of the linked list
        nex = slow.next
        slow.next = None
        pre = slow
        cur = nex
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        
        # check palindrome
        left = A
        right = pre

        while left and right:
            if left.val == right.val:
                left = left.next
                right = right.next
            else:
                return False
        return True


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(2)
l1.next.next.next.next.next = ListNode(1)
solution = PalindromeList()
res = solution.chkPalindrome(l1)
print(res)
