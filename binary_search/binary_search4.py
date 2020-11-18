'''
给出一个转动过的有序数组，你事先不知道该数组转动了多少
(例如,0 1 2 4 5 6 7可能变为4 5 6 7 0 1 2).
在数组中搜索给出的目标值，如果能在数组中找到，返回它的索引，否则返回-1。
假设数组中不存在重复项。
'''

#
#
# @param A int整型一维数组
# @param target int整型
# @return int整型
#
class Solution:
    def search(self , A , target ):
        # write code here
        low, high = 0, len(A) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == A[mid]:
                return mid
            if A[mid] >= A[low]:
                if target >= A[low] and target < A[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                if target > A[mid] and target <= A[high]:
                    low = mid + 1
                else:
                    high = mid
        return -1