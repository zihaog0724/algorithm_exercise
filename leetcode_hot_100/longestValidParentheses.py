# hot100-lc 32. 最长有效括号


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        栈解法题解见https://zhuanlan.zhihu.com/p/555213495
        """
        ret = 0
        stack = [-1]
        for i in range(len(s)):
            if len(stack) == 1 and s[i] == ')':
                stack[0] = i
                continue
            if s[i] == '(':
                stack.append(i)
            else:
                if s[stack[-1]] == '(':
                    ret = max(ret, i - stack[-2])
                    stack.pop()
                else:
                    stack[0] = i
        return ret
