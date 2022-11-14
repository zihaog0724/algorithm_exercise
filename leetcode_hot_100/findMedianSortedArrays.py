# hot100-lc 4. 寻找两个正序数组的中位数

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        """
        核心是把两个有序升序数组做合成, 用归并排序里的merge思路
        """
        merged_arr = self.merge(nums1, nums2)
        if len(merged_arr) % 2 == 0:
            mid = len(merged_arr) // 2
            return (merged_arr[mid] + merged_arr[mid - 1]) * 0.5
        else:
            mid = len(merged_arr) // 2
            return merged_arr[mid]

    def merge(self, nums1, nums2):
        l, r = 0, 0
        new_arr = []
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                new_arr.append(nums1[l])
                l += 1
            else:
                new_arr.append(nums2[r])
                r += 1

        while l < len(nums1):
            new_arr.append(nums1[l])
            l += 1
        while r < len(nums2):
            new_arr.append(nums2[r])
            r += 1
        return new_arr
