# hot100-lc 647. 回文子串

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            ret += 1

        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if (j - i) == 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j]:
                    ret += 1
        return ret
