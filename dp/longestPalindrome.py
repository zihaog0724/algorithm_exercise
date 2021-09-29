# leetcode 5. longestPalindrome

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        left, right = 0, 0
        max_len = 1

        for i in range(len(s)):
            dp[i][i] = True
        
        for j in range(1, len(s)):
            for i in range(j):
                if s[i] == s[j]:
                    if (j - i) <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j]:
                    if (j - i + 1) > max_len:
                        max_len = j - i + 1
                        left, right = i, j
        return s[left:right+1]
