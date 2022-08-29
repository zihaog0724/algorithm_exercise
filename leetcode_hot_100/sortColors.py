# hot100-lc 75. sortColors

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums) - 1)

    def quicksort(self, nums, left, right):
        if left >= right:
            return
        less, more = self.partition(nums, left, right)
        self.quicksort(nums, left, less)
        self.quicksort(nums, more, right)

    def partition(self, nums, left, right):
        less, more = left - 1, right + 1
        cur = left
        pivot = nums[right]
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
        return less, more


def main():
    solution = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)

main()
