# hot100-lc 17. letterComb

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        self.hashmap = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}

        ret = []
        self.backtrace("", digits, 0, ret)
        return ret

    def backtrace(self, combination, digits, digit_idx, ret):
        if digit_idx == len(digits):
            ret.append(combination)
            return
        for letter in self.hashmap[digits[digit_idx]]:
            self.backtrace(combination + letter, digits, digit_idx + 1, ret)
