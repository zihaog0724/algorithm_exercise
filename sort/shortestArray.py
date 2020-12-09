# -*- coding:utf-8 -*-
"""
对于一个无序数组A，请设计一个算法，求出需要排序的最短子数组的长度。

给定一个整数数组A及它的大小n，请返回最短子数组的长度。
"""
class ShortSubsequence:
    def findShortest(self, A, n):
        # write code here
        if n <= 1:
            return 0

        Max = A[0]
        right = 0
        for i in range(1, n):
            if A[i] >= Max:
                Max = A[i]
            else:
                right = i

        if right == 0:
            return 0

        Min = A[-1]
        left = n - 1
        for i in range(n-2, 0, -1):
            if A[i] <= Min:
                Min = A[i]
            else:
                left = i

        return right - left + 1