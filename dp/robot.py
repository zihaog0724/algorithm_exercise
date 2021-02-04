"""
假设有排成一行的N个位置，记为1~N，N一定大于或等于2。
开始时机器人在其中的M位置上（M一定是1~N中的一个），
机器人可以往左走或者往右走，如果机器人来到1位置，那么下一步只能往右来到2位置；
如果机器人来到N位置，那么下一步只能往左来到N-1位置。
规定，机器人必须走K步，最终能来到P位置（P也一定是1~N中的一个）的方法有多少种。
给定4个参数N、M、K、P，返回方法数。
"""

class Solution:
    def walk(self, N, M, K, P):
        # arr dp: (N+1) * (K+1)
        dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
        dp[P][0] = 1
        for col in range(1, K+1):
            for row in range(1, N+1):
                if row == 1:
                    dp[row][col] = dp[2][col-1]
                elif row == N:
                    dp[row][col] = dp[N-1][col-1]
                else:
                    dp[row][col] = dp[row-1][col-1] + dp[row+1][col-1]
        return dp[M][K]

N, M, K, P = 7, 2, 5, 3
solution = Solution()
print(solution.walk(N, M, K, P))
