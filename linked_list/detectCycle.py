'''
对于一个给定的链表，返回环的入口节点，如果没有环，返回null
'''
# 
# @param head ListNode类 
# @return ListNode类
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        # 先检查链表是否为None & 链表是否只有一个元素
        if not head or not head.next:
            return None

        # 快慢指针判断相遇地点，若无环则返回None
        slow = head
        fast = head
        while fast:
            if fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    break
            else:
                return None

        if not fast:
            return None

        """
        判断相遇地点时：
        设a为链表起始到环入口的路程；
        设x为环入口到相遇点的路程；
        设c为环长；
        设slow走过路程为s，则fast走过路程为2s；
        则有s = a + x;
           2s = nc + s;
        推导有a + x = nc；
             a = nc - x = (n - 1)c + (c - x) = kc + (c - x)
        其中，c - x为从相遇点走回环入口的距离。
        则上式意味着，慢指针（step=1）从链表起始出发走过a到环入口的距离，
                    等于快指针（step=1）从相遇点出发走过k圈，再走c-x的距离
        这个c-x的距离恰好使快指针也到达环入口
        """    
        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return fast

# Test
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = l1.next
solution = Solution()
print(solution.detectCycle(l1).val)
