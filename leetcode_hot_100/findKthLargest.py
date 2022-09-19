# hot100-lc 215. findKthLargest

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.qsort(nums, 0, len(nums) - 1)
        return nums[len(nums) - k]

    def qsort(self, nums, left, right):
        if left >= right:
            return
        less, more = self.partition(nums, left, right)
        self.qsort(nums, left, less - 1)
        self.qsort(nums, more + 1, right)

    def partition(self, nums, left, right):
        pivot = nums[right]
        cur, less, more = left, left - 1, right + 1
        while cur < more:
            if nums[cur] < pivot:
                tmp = nums[less + 1]
                nums[less + 1] = nums[cur]
                nums[cur] = tmp
                cur += 1
                less += 1
            elif nums[cur] == pivot:
                cur += 1
            else:
                tmp = nums[more - 1]
                nums[more - 1] = nums[cur]
                nums[cur] = tmp
                more -= 1
        return less + 1, more - 1
