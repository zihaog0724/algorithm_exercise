# leetcode 17. letterCombinations

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
            
        hashmap = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}
        res = []
        self.backtrack("", digits, hashmap, res)
        return res

    def backtrack(self, combination, next_digits, hashmap, res):
        if len(next_digits) == 0:
            res.append(combination)
            return
        for letter in hashmap[next_digits[0]]:
            self.backtrack(combination + letter, next_digits[1:], hashmap, res)
