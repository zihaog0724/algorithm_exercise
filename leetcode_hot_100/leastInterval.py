# hot100-lc 621. 任务调度器


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        """
        ['A', 'A', 'A', 'B', 'B', 'B'], n = 2
        先把最多次数的任务排好，A->单位时间->单位时间->A->单位时间->单位时间->
        这一步需要的时间为(出现最多次数的任务 - 1) * (n + 1)
        再加上出现最多次数的任务个数
        """
        dct = {}
        for t in tasks:
            if t not in dct:
                dct[t] = 1
            else:
                dct[t] += 1

        freq = sorted(dct.values())
        max_freq = freq[-1]
        n_max = freq.count(max_freq)
        return max((max_freq - 1) * (n + 1) + n_max, len(tasks))
