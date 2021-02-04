"""
假设农场中成熟的母牛每年只会生 1 头小母牛，并且永远不会死。
第一年农场中有一只成熟的母牛，从第二年开始，母牛开始生小母牛。
每只小母牛 3 年之后成熟又可以生小母牛。给定整数 n，求出 n 年后牛的数量。
"""

class Solution:
    def num_cows(self, n):
        return self.process(n)

    def process(self, n):
        if n == 1 or n == 2 or n == 3:
            return n
        return self.process(n-1) + self.process(n-3)

n = 20
solution = Solution()
print(solution.num_cows(n))
