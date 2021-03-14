"""
问题描述：给定两个序列：X[1...m]和Y[1...n]，求在两个序列中同时出现的最长子序列的长度。
"""

class Solution:
    def process(self, str1, str2, m, n):
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
 
str1 = "ABCBDAB"
str2 = "BDCABA"
solution = Solution()
print(solution.process(str1, str2, len(str1), len(str2)))
