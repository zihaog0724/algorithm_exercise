# 给出一组区间，请合并所有重叠的区间。
# input e.g. [[10,30],[20,60],[80,100],[150,180]]
# output e.g. [[10,60],[80,100],[150,180]]

#
# @param intervals Interval类一维数组 
# @return Interval类一维数组
#

class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b

class Solution:
    def merge(self , intervals):
        # write code here
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key = lambda x: x.start)

        merged = []
        for i in intervals:
            if len(merged) == 0 or i.start > merged[-1].end:
                merged.append(i)
            elif i.start <= merged[-1].end:
                if i.end <= merged[-1].end:
                    continue
                else:
                    merged[-1].end = i.end
        return merged

# Test
interval1 = Interval(50, 60)
interval2 = Interval(20, 60)
interval3 = Interval(50, 100)
interval4 = Interval(80, 120)
solution = Solution()

print(solution.merge([interval1, interval2, interval3, interval4])[0].start)
print(solution.merge([interval1, interval2, interval3, interval4])[0].end)       