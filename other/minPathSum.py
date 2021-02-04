"""
给定一个 n * m 的矩阵 a，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，
路径上所有的数字累加起来就是路径和，输出所有的路径中最小的路径和。
"""
class Solution:
    def minPathSum(self, arr, n, m):
        return self.process(arr, 0, 0, n, m)

    def process(self, arr, x, y, n, m):
        if x == m - 1 and y == n - 1:
            return arr[x][y]

        cur = arr[x][y]

        if x == m - 1:
            return cur + self.process(arr, x, y+1, n, m)

        if y == n - 1:
            return cur + self.process(arr, x+1, y, n, m)

        return cur + min(self.process(arr, x+1, y, n, m), self.process(arr, x, y+1, n, m))


arr = [[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]]
n, m = 4, 4
solution = Solution()
print(solution.minPathSum(arr, n, m))
