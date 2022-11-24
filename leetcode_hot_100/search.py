# hot100-lc 33. 搜索旋转排序数组

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        搜索旋转排序数组O(logN)思路
        因为数组是排序后旋转过的, 因此low~mid和mid~high肯定有一个是有序的
        判断出来有序的那个区间, 然后用常规二分思路搜索目标即可
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return target
            if nums[mid] >= nums[low]:  # 说明low~mid有序
                if nums[low] <= target <= nums[mid]:  # 说明target在low~mid这个有序区间内
                    high = mid
                else:  # 说明target不在low~mid这个有序区间内
                    low = mid + 1
            else:  # 说明low~mid无序, 即mid~high有序
                if nums[mid] <= target <= nums[high]:  # 说明target在mid~high这个有序区间内
                    low = mid
                else:  # 说明target不在mid~high这个有序区间内
                    high = mid - 1
        return -1
