# hot100-lc 31. nextPermutation

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        例子:
        1234 1243 1324 1342 1423 1432
        2134 2143 2314 2341 2413 2431
        3124 3142 3214 3241 3412 3421
        4123 4132 4213 4231 4312 4321
        看规律:
        1. 如果nums是纯降序, 直接逆序即可
        2. 如果不是纯降序, 也就是倒序遍历nums不是纯升序的话,
           还是倒序遍历nums, 找到使遍历不为升序的元素的idx记为i, 再找到i后面的j, 这里的j为倒序遍历时第一个nums[j]比nums[i]大的下标
           交换nums[i]和nums[j], 再把下标i后面逆序
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
