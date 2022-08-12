# hot100-3

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        tmp = []
        max_len = 0
        cur_len = 0
        for i in range(len(s)):
            if s[i] not in tmp:
                tmp.append(s[i])
                cur_len += 1
            else:
                if cur_len >= max_len:
                    max_len = cur_len
                idx = len(tmp) - 1 - tmp[::-1].index(s[i])
                tmp = tmp[idx+1:]
                tmp.append(s[i])
                cur_len = len(tmp)
        if cur_len >= max_len:
            max_len = cur_len
        return max_len
