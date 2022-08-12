# hot100-1

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, value in enumerate(nums):
            for j in range(i+1, len(nums)):
                if (value + nums[j]) == target:
                    return i, j
