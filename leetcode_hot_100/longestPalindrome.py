# hot100-lc 5. 最长回文子串


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        动态规划:
        dp[i][j]含义为[i, j]闭区间内的子串是否回文
        因此只需要更新j >= i的格子即可
        更新分两种情况，第一种为j-i等于1，这时候只需要判断s[i]和s[j]是否相等
        另一种是j-i大于1，这时候需要根据dp[i+1][j-1]来判断
        """
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        max_len = 0
        ret_i, ret_j = 0, 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if (j - i) == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    if dp[i+1][j-1] and s[i] == s[j]:
                        dp[i][j] = True
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        ret_i = i
                        ret_j = j
        return s[ret_i:ret_j+1]
        
