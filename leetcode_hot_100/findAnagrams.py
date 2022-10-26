# hot100-lc 438. 找到字符串中所有字母异位词

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        """
        p中各字母的统计个数，和s中与p相同长度的子串的各字母统计个数相同即可
        """
        p_len, s_len = len(p), len(s)
        count_p = {}
        for c in p:
            if c not in count_p.keys():
                count_p[c] = 1
            else:
                count_p[c] += 1

        count_s = {}
        left = 0
        ret = []
        for i in range(s_len):
            if s[i] not in count_s:
                count_s[s[i]] = 1
            else:
                count_s[s[i]] += 1
            if (i - left + 1) == p_len:
                if count_s == count_p:
                    ret.append(left)
                count_s[s[left]] -= 1
                if count_s[s[left]] == 0:
                    del count_s[s[left]]
                left += 1
        return ret
