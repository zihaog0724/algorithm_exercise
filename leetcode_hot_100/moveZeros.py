# hot100-lc 283. 移动零

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cursor = -1  # 非零区
        cur = 0
        while cur < len(nums):
            if nums[cur] != 0:
                tmp = nums[cur]
                nums[cur] = nums[cursor+1]
                nums[cursor+1] = tmp
                cursor += 1
                cur += 1
            else:
                cur += 1
