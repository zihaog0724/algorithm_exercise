# leetcode 75. sortColors

class Solution(object):
    def sortColors(self, nums):
        self.qsort(nums, 0, len(nums)-1)

    def qsort(self, nums, left, right):
        if left >= right:
            return
        less, more = self.partition(nums, left, right)
        self.qsort(nums, left, less)
        self.qsort(nums, more, right)

    def partition(self, nums, left, right):
        less, cur, more = left-1, left, right+1
        pivot = nums[right]
        while cur < more:
            if nums[cur] < pivot:
                tmp = nums[less+1]
                nums[less+1] = nums[cur]
                nums[cur] = tmp
                less += 1
                cur += 1
            elif nums[cur] == pivot:
                cur += 1
            else:
                tmp = nums[more-1]
                nums[more-1] = nums[cur]
                nums[cur] = tmp
                more -= 1
        return less, more
