'''
有 N 个网络节点，标记为 1 到 N。
给定一个列表 times，表示信号经过有向边的传递时间。 
times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w 是一个信号从源节点传递到目标节点的时间。
现在，我们向当前的节点 K 发送了一个信号。需要多久才能使所有节点都收到信号？
如果不能使所有节点收到信号，返回 -1。
'''

class Solution:
    def networkDelayTime(self, time, N, K):
        graph = {}
        for u, v, w in times:
            graph[u] = graph.get(u, {})
            graph[u][v] = w

        if K not in graph:
            return -1

        distances = []
        points = []
        for i in range(1, N+1):
            if K == i:
                distances.append(0)
            else:
                distances.append(graph[K].get(i, float("inf")))
                if i in graph:
                    points.append(i)

        while points:
            cur_point = points.pop(0)
            for i in graph[cur_point]:
                if graph[cur_point][i] + distances[cur_point-1] < distances[i-1]:
                    distances[i-1] = graph[cur_point][i] + distances[cur_point-1]

        max_time = max(distances)
        if max_time == float("inf"):
            return -1
        return max_time

N = 5
K = 1
times = [[1,2,1],[1,3,7],[1,4,10],[2,3,2],[2,5,50],[3,4,5],[3,5,20],[4,5,3]]
solution = Solution()
print(solution.networkDelayTime(times, N, K))


