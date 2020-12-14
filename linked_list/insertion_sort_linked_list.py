# 使用插入排序对链表进行排序

# 
# @param head ListNode类 
# @return ListNode类
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        # write code here
        if not head or not head.next:
            return head
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        sorted_arr = self.sort(arr)

        L = ListNode(0)
        new_head = L
        for i in sorted_arr:
            L.next = ListNode(i)
            L = L.next
        return new_head.next

    def sort(self, arr):
        for i in range(1, len(arr)):
            j = i - 1
            while j >= 0:
                if arr[j+1] < arr[j]:
                    tmp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = tmp
                    j -= 1
                else:
                    break
        return arr

# Test
l1 = ListNode(6)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(5)
l1.next.next.next.next = ListNode(1)
solution = Solution()
print(solution.insertionSortList(l1).next.next.val)