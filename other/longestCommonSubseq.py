"""
问题描述：给定两个序列：X[1...m]和Y[1...n]，求在两个序列中同时出现的最长子序列的长度。
"""

class Solution:
    def process(self, str1, str2, m, n):
        if m == 0 or n == 0:
            return 0
        if str1[m-1] == str2[n-1]:
            return self.process(str1, str2, m-1, n-1) + 1
        return max(self.process(str1, str2, m-1, n), self.process(str1, str2, m, n-1))
        

str1 = "ABCBDAB"
str2 = "BDCABA"
solution = Solution()
print(solution.process(str1, str2, len(str1), len(str2)))
