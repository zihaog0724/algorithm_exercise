# hot100-lc 139. 单词拆分

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(len(s)):
            if not dp[i]:
                continue
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]
