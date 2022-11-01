# hot100-lc 581. 最短无序连续子数组

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = self.merge_sort(nums)
        left, right = 0, len(nums) - 1
        while left <= right and nums[left] == sorted_nums[left]:
            left += 1
        while left <= right and nums[right] == sorted_nums[right]:
            right -= 1
        return right - left + 1

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        arr_left = self.merge_sort(arr[:mid])
        arr_right = self.merge_sort(arr[mid:])
        return self.merge(arr_left, arr_right)

    def merge(self, arr_left, arr_right):
        l, r = 0, 0
        new_arr = []
        while l < len(arr_left) and r < len(arr_right):
            if arr_left[l] < arr_right[r]:
                new_arr.append(arr_left[l])
                l += 1
            else:
                new_arr.append(arr_right[r])
                r += 1

        while l < len(arr_left):
            new_arr.append(arr_left[l])
            l += 1

        while r < len(arr_right):
            new_arr.append(arr_right[r])
            r += 1
        return new_arr
