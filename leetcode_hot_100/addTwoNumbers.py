# hot100-lc 2. 两数相加

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
        """
        先把l1和l2代表的数字的和算出来
        再接到新链表上
        """
        l1_total = self.get_list_val(l1)
        l2_total = self.get_list_val(l2)
        total = l1_total + l2_total
        lst = [i for i in str(total)]
        cur = ListNode(0)
        ret = cur
        for i in range(len(lst) - 1, -1, -1):
            cur.next = ListNode(int(lst[i]))
            cur = cur.next
        return ret.next

    def get_list_val(self, l):
        total = 0
        n = 0
        while l:
            total += l.val * (10 ** n)
            l = l.next
            n += 1
        return total
