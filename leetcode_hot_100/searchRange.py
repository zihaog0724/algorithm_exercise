# hot100-lc 34. 在排序数组中查找元素的第一个和最后一个位置

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        要求时间复杂度O(logN), 思路自然是用二分
        分别用两次二分找到左边界和右边界, 边界条件还是各种尝试
        注意找右边界的时候, 求mid的时候要(low + high + 1) // 2, 不加1的话会死循环
        """
        if len(nums) == 0:
            return [-1, -1]
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if target <= nums[mid]:
                high = mid
            else:
                low = mid + 1
        if nums[low] != target:
            return [-1, -1]
        l = low

        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high + 1) // 2
            if target >= nums[mid]:
                low = mid
            else:
                high = mid - 1
        if nums[high] != target:
            return [-1, -1]
        r = high
        return [l, r]
