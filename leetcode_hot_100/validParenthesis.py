# hot100-lc 20. validParenthesis

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap = {"(": ")",
                   "[": "]",
                   "{": "}"}

        if len(s) % 2 != 0:
            return False

        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append(char)
                continue
            if char in hashmap.keys():
                stack.append(char)
            else:
                if stack[-1] in hashmap.keys() and hashmap[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
