# hot100-3. 无重复字符的最长子串


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        开一tmp数组用于存放当前遍历到的字符
        遍历s, 如果当前字符不在tmp中,说明现在还是无重复
        反之说明有重复了, 需要找到tmp中重复字符对应的idx,
        把重复字符之前的都干掉, 让tmp不重复, 继续遍历
        """
        ret = 0
        if len(s) == 0:
            return ret

        tmp = []
        cur_len = 0
        for i in range(len(s)):
            if s[i] not in tmp:
                tmp.append(s[i])
                cur_len += 1
                if cur_len > ret:
                    ret = cur_len
            else:
                idx = tmp.index(s[i])
                tmp = tmp[idx+1:]
                tmp.append(s[i])
                cur_len = len(tmp)
        return ret
