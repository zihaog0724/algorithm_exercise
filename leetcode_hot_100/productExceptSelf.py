# hot100-lc 238. productExceptSelf

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [1 for i in range(len(nums))]
        k = 1
        for i in range(len(nums)):
            if i > 0:
                ret[i] = k
            k = k * nums[i]

        k = 1
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1:
                ret[i] = ret[i] * k
            k = k * nums[i]
        return ret
