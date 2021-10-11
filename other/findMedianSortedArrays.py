# leetcode 4. findMedianSortedArrays

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l, r = 0, 0
        n1, n2 = len(nums1), len(nums2)
        arr = []
        while l < n1 and r < n2:
            if nums1[l] <= nums2[r]:
                arr.append(nums1[l])
                l += 1
            else:
                arr.append(nums2[r])
                r += 1
        
        while l < n1:
            arr.append(nums1[l])
            l += 1

        while r < n2:
            arr.append(nums2[r])
            r += 1

        if (len(arr) % 2) != 0:
            return arr[len(arr)//2]
        else:
            return (arr[len(arr) / 2] + arr[len(arr) / 2 - 1]) * 0.5 
