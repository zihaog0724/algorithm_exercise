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
        dp = [[0 for _ in range(aim+1)] for _ in range(len(arr)+1)]
        dp[-1][0] = 1
        for i in range(len(arr))[::-1]:
            cur = arr[i]
            for j in range(aim+1):
                if j - cur >= 0:
                    dp[i][j] = dp[i+1][j] + dp[i][j-cur]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][aim]
                

arr = [5,2,3,1]
aim = 350
solution = Solution()
print(solution.ways(arr, aim))
