'''
请写出一个高效的在m*n矩阵中判断目标值是否存在的算法，矩阵具有如下特征：
每一行的数字都从左到右排序
每一行的第一个数字都比上一行最后一个数字大
例如：
对于下面的矩阵：
[
    [1,   3,  5,  9],
    [10, 11, 12, 30],
    [230, 300, 350, 500]
]
要搜索的目标值为3，返回true；
'''

class Solution:
    def searchMatrix(self , matrix , target ):
        # write code here
        # 先判断target是否超出矩阵范围
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        # 二分确定行
        low1, high1 = 0, len(matrix) - 1
        while low1 <= high1:
            mid1 = (low1 + high1) // 2
            if target == matrix[mid1][0]:
                return True
            if target < matrix[mid1][0]:
                high1 = mid1 - 1
            else:
                low1 = mid1 + 1

        # 二分确定列
        low2, high2 = 0, len(matrix[0]) - 1
        while low2 <= high2:
            mid2 = (low2 + high2) // 2
            if target == matrix[mid1][mid2]:
                return True
            if target < matrix[mid1][mid2]:
                high2 = mid2 - 1
            else:
                low2 = mid2 + 1

        return False

# Test
solution = Solution()
res = solution.searchMatrix([[1,3]],3)
print(res)




        
