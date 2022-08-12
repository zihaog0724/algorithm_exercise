# hot100-lc 5.


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        l, r = 0, 0
        max_len = 1
        for j in range(1, len(s)):
            for i in range(j):
                if s[i] == s[j]:
                    if (j - i) <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        l, r = i, j
        return s[l:r+1]

        
