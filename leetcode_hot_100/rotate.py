# hot100-lc 48. 旋转图像

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        先以左上-右下对角线为轴做一次翻转, 在以竖直中线为轴做一次翻转
        1 2 3             1 4 7             7 4 1
        4 5 6  第一次翻转-> 2 5 8 第二次翻转->  8 5 2
        7 8 9             3 6 9             9 6 3
        """
        n = len(matrix)
        for row in range(n - 1):
            for col in range(row + 1, n):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = tmp

        mid = n // 2
        for row in range(n):
            for col in range(mid):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[row][n - col - 1]
                matrix[row][n - col - 1] = tmp
