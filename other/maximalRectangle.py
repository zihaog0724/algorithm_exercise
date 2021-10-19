# leetcode 85. maximalRectangle

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        matrix = [[int(i) for i in x] for x in matrix]
        res = 0
        for i in range(len(matrix)):
            res = self.find(matrix[:i+1], res)
        return res

    def find(self, matrix, res):
        array = [0]
        for m in range(len(matrix[0])):
            n = len(matrix) - 1
            v = 0
            while n >= 0 and matrix[n][m] == 1:
                n -= 1
                v += 1
            array.append(v)
        array.append(0)
        
        stack = []
        for i in range(len(array)):
            while len(stack) > 0 and array[stack[-1]] > array[i]:
                num = array[stack.pop()]
                res = max(res, num * (i - stack[-1] - 1))
            stack.append(i)
        return res
