'''
现在你总共有 n 门课需要选，记为 0 到 n-1。
在选修某些课程之前需要一些先修课程。 
例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？

示例 1:

输入: 2, [[1,0]] 
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；
    并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
'''
class Solution:
    def canFinish(self, numCourses, prerequisites):
        dic = {}
        for i in range(numCourses):
            dic[i] = 0

        for i in range(len(prerequisites)):
            head = prerequisites[i][1]
            tail = prerequisites[i][0]
            dic[tail] += 1  

        queue = []
        for i in range(len(dic)):
            if dic[i] == 0:
                queue.append(i)

        res = []
        while len(queue) > 0:
            node = queue.pop(0)
            res.append(node)
            for i in range(len(prerequisites)):
                if prerequisites[i][1] == node:
                    cur_tail = prerequisites[i][0]
                    dic[cur_tail] -= 1
                    if dic[cur_tail] == 0:
                        queue.append(cur_tail)

        if len(res) == numCourses:
            return True
        else:
            return False


numCourses = 2
prerequisites = [[1,0],[0,1]]
solution = Solution()
print(solution.canFinish(numCourses, prerequisites))