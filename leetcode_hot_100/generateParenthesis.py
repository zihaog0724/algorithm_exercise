# hot100-lc 22.

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.n = n
        res = []
        cur = "("
        self.backtrace(cur, 1, 0, res)
        return res

    def backtrace(self, cur, left, right, res):
        if right > left:
            return
        if left > self.n:
            return
        if len(cur) == self.n * 2:
            res.append(cur)
            return
        self.backtrace(cur+"(", left+1, right, res)
        self.backtrace(cur+")", left, right+1, res)
