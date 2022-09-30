# hot100-lc 240. 搜索二维矩阵

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        for i in range(len(matrix)):
            ret = self.binary_search(matrix[i], target)
            if ret:
                return True
        return False
        
    def binary_search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return True
        return False
