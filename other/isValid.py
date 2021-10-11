# leetcode 20. validParenthesis

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap = {"(" : ")",
                   "[" : "]",
                   "{" : "}"}
        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append(char)
                continue
            if stack[-1] not in hashmap.keys():
                return False
            if char != hashmap[stack[-1]]:
                stack.append(char)
                continue
            else:
                stack.pop()
        return len(stack) == 0
