# 给定一个无序单链表，实现单链表的选择排序(按升序排序)。

# 
# @param head ListNode类 the head node
# @return ListNode类
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortInList(self, head):
        # write code here
        if not head:
            return None
        if not head.next:
            return head

        array = []
        l = head
        while l:
            array.append(l.val)
            l = l.next

        sorted_array = self.qsort(array)
        l2 = head
        for i in sorted_array:
            l2.val = i
            l2 = l2.next
        return head

    def qsort(self, array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
            return self.qsort(less) + [pivot] + self.qsort(greater)


# Test
l1 = ListNode(5)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(1)
l1.next.next.next.next = ListNode(4)

solution = Solution()
print(solution.sortInList(l1).next.next.next.next.val)

s = "(2*(3-4))*5"
print(eval(s))
