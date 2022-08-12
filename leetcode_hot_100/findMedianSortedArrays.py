# hot100-4


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l, r = 0, 0
        merged_arr = []
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                merged_arr.append(nums1[l])
                l += 1
            else:
                merged_arr.append(nums2[r])
                r += 1
        while l < len(nums1):
            merged_arr.append(nums1[l])
            l += 1
        while r < len(nums2):
            merged_arr.append(nums2[r])
            r += 1
        print(merged_arr)
        if len(merged_arr) % 2 == 0:
            mid = len(merged_arr) // 2 - 1
            return 0.5 * (merged_arr[mid] + merged_arr[mid+1])
        else:
            mid = len(merged_arr) // 2
            return merged_arr[mid]
