# hot100-lc 85. 

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ret = 0
        rows, cols = len(matrix), len(matrix[0])
        matrix = [[int(x) for x in row] for row in matrix]
        heights = matrix[0]
        for i in range(rows):
            if i == 0:
                ret = max(ret, self.find_histogram(heights))
            else:
                for j in range(cols):
                    heights[j] = heights[j] + matrix[i][j] if matrix[i][j] != 0 else matrix[i][j]
                ret = max(ret, self.find_histogram(heights))
        return ret

    def find_histogram(self, heights):
        ret = 0
        stack = []
        i = 0
        while i < len(heights):
            if len(stack) == 0:
                stack.append(i)
                i += 1
                continue
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
                i += 1
            elif heights[i] < heights[stack[-1]]:
                left = stack[-1]
                while left >= 0:
                    if heights[left] < heights[stack[-1]]:
                        break
                    left -= 1
                ret = max(ret, heights[stack[-1]] * (i - left - 1))
                stack.pop()
            else:
                i += 1

        for pos in stack:
            left = pos
            while left >= 0:
                if heights[left] < heights[pos]:
                    break
                left -= 1
            ret = max(ret, heights[pos] * (i - left - 1))
        return ret
