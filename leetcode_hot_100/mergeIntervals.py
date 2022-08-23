# hot100-lc 56. mergeIntervals

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        ret = [intervals[0]]
        for i in range(1, len(intervals)):
            interval1, interval2 = ret[-1], intervals[i]
            if interval2[0] > interval1[1]:
                ret.append(interval2)
            else:
                if interval1[1] <= interval2[1]:
                    ret[-1][1] = interval2[1]
                else:
                    ret[-1][1] = interval1[1]
        return ret
