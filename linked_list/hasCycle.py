'''
判断给定的链表中是否有环
'''
# 
# @param head ListNode类 
# @return bool布尔型
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        # write code here
        # 先判断空链表或链表中只有一个元素
        if not head or not head.next:
            return False

        # 快慢指针判断是否有cycle：快指针每次走两步，慢指针每次走一步，若有环终会相遇
        slow = head 
        fast = head.next
        while slow != fast: # 若两指针相同证明相遇，跳出循环返回True
            if fast.next is None or fast.next.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

# Test
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
#l1.next.next.next = l1.next
solution = Solution()
print(solution.hasCycle(l1))