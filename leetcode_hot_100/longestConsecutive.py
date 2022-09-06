# hot100-lc 128. 最长连续序列

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        ret = 1
        tmp = 1
        max_value = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - max_value == 1:
                tmp += 1
                ret = max(ret, tmp)
                max_value = nums[i]
            elif nums[i] - max_value < 1:
                continue
            else:
                tmp = 1
                max_value = nums[i]
        return ret
