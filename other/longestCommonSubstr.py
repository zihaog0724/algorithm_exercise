"""
问题描述：给定两个序列：X[1...m]和Y[1...n]，求在两个序列中同时出现的最长子串的长度。
"""

class Solution:
    def process(self, str1, str2, m, n, cnt):
        global max_cnt
        if m == 0 or n == 0:
            return 0
        if str1[m-1] == str2[n-1]:
            if cnt + 1 > max_cnt:
                max_cnt += 1
            self.process(str1, str2, m-1, n-1, cnt+1) + 1
        else:
            self.process(str1, str2, m-1, n, 0)
            self.process(str1, str2, m, n-1, 0)
        return max_cnt

max_cnt = 0
str1 = "ABCBDAB"
str2 = "ABCB"
solution = Solution()
print(solution.process(str1, str2, len(str1), len(str2), 0))
