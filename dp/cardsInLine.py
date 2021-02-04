"""
题目：有一个整型数组A，代表数值不同的纸牌排成一条线。
玩家a和玩家b依次拿走每张纸牌，规定玩家a先拿，玩家b后拿，
但是每个玩家每次只能拿走最左或最右的纸牌，玩家a和玩家b都绝顶聪明，他们总会采用最优策略。
请返回最后获胜者的分数。给定纸牌序列A及序列的大小n，请返回最后分数较高者得分数(相同则返回任意一个分数)。

测试样例：
[1,2,100,4],4
返回：101
"""

class Solution:
    def win(self, arr, N):
        dp1 = [[0 for _ in range(N)] for _ in range(N)]
        dp2 = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            dp1[i][i] = arr[i]

        for R in range(1, N):
            L = 0
            while L < N and R < N:
                dp1[L][R] = max(arr[L] + dp2[L+1][R], arr[R] + dp2[L][R-1])
                dp2[L][R] = min(dp1[L+1][R], dp1[L][R-1])
                L += 1
                R += 1
        return max(dp1[0][N-1], dp2[0][N-1])

arr = [1,2,100,4]
N = 4
solution = Solution()
print(solution.win(arr, N))
