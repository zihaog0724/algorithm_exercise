# hot100-lc 15. threeSum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        if len(nums) < 3:
            return ret
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            anchor = nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                if (anchor + nums[left] + nums[right]) == 0:
                    ret.append([anchor, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif (anchor + nums[left] + nums[right]) > 0:
                    right -= 1
                else:
                    left += 1
        return ret
