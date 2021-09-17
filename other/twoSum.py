# leetcode 1. two sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dic and dic[diff] != i:
                return [i, dic[diff]]
