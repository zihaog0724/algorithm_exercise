# leetcode 3. lengthOfLongestSubstring

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        queue = set()
        left = 0
        cur_len = 0
        max_len = 0
        for i in range(n):
            while s[i] in queue:
                queue.remove(s[left])
                cur_len -= 1
                left += 1
            queue.add(s[i])
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
        return max_len
