# hot100-lc 152. maxProduct

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        max_value = nums[0]
        min_value = nums[0]
        ret = max_value
        for i in range(1, len(nums)):
            tmp = max_value
            max_value = max(nums[i], nums[i] * max_value, nums[i] * min_value)
            min_value = min(nums[i], nums[i] * min_value, nums[i] * tmp)
            ret = max(max_value, ret)
        return ret
