# leetcode 22. generateParenthesis

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.n = n
        cur = "("
        self.backtrack(1, 0, cur, res)
        return res

    def backtrack(self, left, right, cur, res):
        if right > left:
            return
        if left > self.n:
            return
        if len(cur) == self.n * 2:
            res.append(cur)
            return
        self.backtrack(left+1, right, cur+"(", res)
        self.backtrack(left, right+1, cur+")", res)

