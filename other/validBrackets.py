"""
给定一个数组arr，返回arr的最长无的重复子串的长度(无重复指的是所有数字都不相同)。
"""

class Solution:
    def isValid(self , s):
        # write code here
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            elif i in "([{":
                stack.append(i)
            elif i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False

        if not stack:
            return True
        return False

solution = Solution()
arr = "((())"
print(solution.isValid(arr))
