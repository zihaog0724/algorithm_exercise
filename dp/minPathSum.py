"""
给定一个 n * m 的矩阵 a，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，
路径上所有的数字累加起来就是路径和，输出所有的路径中最小的路径和。
"""

class Solution:
    def minPathSum(self, arr, n, m):
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[-1][-1] = arr[-1][-1]

        for j in range(m-1)[::-1]:
            dp[-1][j] = arr[-1][j] + dp[-1][j+1]

        for i in range(n-1)[::-1]:
            dp[i][-1] = arr[i][-1] + dp[i+1][-1]

        for row in range(n-1)[::-1]:
            for col in range(m-1)[::-1]:
                dp[row][col] = arr[row][col] + min(dp[row+1][col], dp[row][col+1])
        return dp[0][0]


arr = [[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]]
n, m = 4, 4
solution = Solution()
print(solution.minPathSum(arr, n, m))
