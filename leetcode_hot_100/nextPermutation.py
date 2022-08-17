# hot100-lc 31. nextPermutation

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1

        if i == 0:
            nums[:] = nums[::-1]

        else:
            i = i - 1
            j = len(nums) - 1
            while j > i:
                if nums[j] > nums[i]:
                    break
                j -= 1

            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            nums[i+1:] = nums[i+1:][::-1]
