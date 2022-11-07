# hot100-lc 739. 每日温度

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ret = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            if len(stack) == 0 or temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
                continue
            while len(stack) > 0:
                if temperatures[i] > temperatures[stack[-1]]:
                    ret[stack[-1]] = i - stack[-1]
                    stack.pop()
                else:
                    break
            stack.append(i)
        return ret
