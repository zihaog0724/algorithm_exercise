# hot100-lc 448. 找到所有数组中消失的数字

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        把nums中元素值当作下标，该下标位置的元素变成负数，操作完之后没有变成负数的位置就是缺失值
        """
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                continue
            nums[abs(nums[i]) - 1] *= -1

        ret = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ret.append(i + 1)
        return ret
