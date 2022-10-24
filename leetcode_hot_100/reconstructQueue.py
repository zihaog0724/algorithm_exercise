# hot100-lc 406. 根据身高重建队列

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 身高降序排序，相同身高按people[1]升序排列
        people = sorted(people, key=cmp_to_key(self.cmp))
        ret = []
        for i in people:
            ret.insert(i[1], i)
        return ret

    @staticmethod
    def cmp(x, y):
        if x[0] > y[0]:
            return -1
        elif x[0] < y[0]:
            return 1
        else:
            if x[1] < y[1]:
                return -1
            else:
                return 1

