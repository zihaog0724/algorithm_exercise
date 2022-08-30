# hot100-lc 84. largestRectangleArea

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
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
                continue

        for pos in stack:
            left = pos
            h = heights[pos]
            while left >= 0:
                if heights[left] < h:
                    break
                left -= 1
            ret = max(ret, heights[pos] * (i - left - 1))
        return ret
