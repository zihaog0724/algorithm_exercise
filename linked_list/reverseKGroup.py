'''
将给出的链表中的节点每k个一组翻转，返回翻转后的链表
如果链表中的节点数不是k的倍数，将最后剩下的节点保持原样
你不能更改节点中的值，只能更改节点本身。
要求空间复杂度O(1)
例如：
给定的链表是1→2→3→4→5
对于k=2, 你应该返回2→1→4→3→5
对于k=3, 你应该返回3→2→1→4→5
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self , head , k):
        # write code here
        node = head
        for i in range(k):
            if not node:
                return head
            node = node.next
        newhead = self.reverse(head, node)
        head.next = self.reverseKGroup(node, k)
        return newhead

    def reverse(self, head, node):
        cur = head
        pre = None
        nex = None
        while cur != node:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre



# Test
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
solution = Solution()
print(solution.reverseKGroup(l1, 2).next.next.val)