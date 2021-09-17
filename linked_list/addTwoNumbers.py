# leetcode 2. addTwoNumbers

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_num = 0
        n = 0
        while l1:
            l1_num += l1.val * 10**n
            l1 = l1.next
            n += 1

        l2_num = 0
        n = 0
        while l2:
            l2_num += l2.val * 10**n
            l2 = l2.next
            n += 1

        sum = str(l1_num + l2_num)
        length = len(sum)
        res = ListNode(int(sum[-1]))
        cur = res
        for i in range(length-2, -1, -1):
            cur.next = ListNode(int(sum[i]))
            cur = cur.next
        return res
