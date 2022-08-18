# hot100-lc 32. longestValidParentheses

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        stack = [-1]
        for i in range(len(s)):
            if len(stack) == 1 and s[i] == ")":  # 栈长度为1且碰到右括号，更新栈底
                stack[0] = i
                continue
            if s[i] == "(":  # 碰到左括号，无脑压栈
                stack.append(i)
            else:  # 栈长度不唯一且碰到右括号
                if s[stack[-1]] == "(":  # 如果前一个是左括号
                    ret = max(ret, i - stack[-2])
                    stack.pop()
                else:  # 如果前一个是右括号，继续更新栈底
                    stack[0] = i
        return ret
