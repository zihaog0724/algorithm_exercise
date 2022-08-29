# hot100-lc 76. minWindow

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        lookup = {}
        for c in t:  # 含义为target中的字符key还剩下多少个没有被匹配到
            if c not in lookup:
                lookup[c] = 1
            else:
                lookup[c] += 1
        ret = ""
        ret_len = 100000
        left, right = -1, -1
        while right < len(s):
            move_left, move_right = True, False
            for key, value in lookup.items():
                if value > 0:  # 如果还有没被匹配到的，那就还需要移动右指针，增大搜索范围
                    move_left, move_right = False, True
                    break
            if move_right:
                right += 1
                if right == len(s):
                    break
                if s[right] in t:
                    lookup[s[right]] -= 1
            if move_left:  # 如果需要移动左指针了，说明此时target中全部字符已被覆盖
                tmp_ret = s[left+1:right+1]
                if len(tmp_ret) < ret_len:
                    ret = tmp_ret
                    ret_len = len(tmp_ret)
                left += 1
                if s[left] in t:
                    lookup[s[left]] += 1
        return ret
