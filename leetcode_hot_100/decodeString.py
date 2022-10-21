# hot100-lc 394. 字符串解码

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if c == ']':
                repeat_str = ''
                repeat_cnt = ''
                while stack and stack[-1] != '[':
                    repeat_str = stack.pop() + repeat_str
                stack.pop()
                while stack and stack[-1].isnumeric():
                    repeat_cnt = stack.pop() + repeat_cnt
                stack.append(repeat_str * int(repeat_cnt))
            else:
                stack.append(c)
        return ''.join(stack)
