# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            res = 0
            for i in range(2, n+1):
                res = a + b
                a = b
                b = res
            return res