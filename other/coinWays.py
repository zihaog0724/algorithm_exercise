"""
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。
假设每一种面额的硬币有无限个。

示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""

class Solution:
    def ways(self, arr, aim):
        return self.process(arr, 0, aim)

    def process(self, arr, index, rest):
        if index == len(arr):
            if rest == 0:
                return 1
            else:
                return 0

        nums = 0
        ways = 0
        while nums * arr[index] <= rest:
            ways += self.process(arr, index + 1, rest - nums * arr[index])
            nums += 1
        return ways

arr = [5,2,3,1]
aim = 350
solution = Solution()
print(solution.ways(arr, aim))
