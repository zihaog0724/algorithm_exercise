# hot100-lc 207. 课程表

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        dic = {}  # 存储每门课程的入度数量
        for i in range(numCourses):
            dic[i] = 0

        for pre in prerequisites:
            tail = pre[0]
            dic[tail] += 1

        queue = []
        for k, v in dic.items():
            if v == 0:
                queue.append(k)

        course_taken = []
        while len(queue) > 0:
            course = queue.pop()
            course_taken.append(course)
            for pre in prerequisites:
                head, tail = pre[1], pre[0]
                if head == course:
                    dic[tail] -= 1
                    if dic[tail] == 0:
                        queue.append(tail)
        return len(course_taken) == numCourses
