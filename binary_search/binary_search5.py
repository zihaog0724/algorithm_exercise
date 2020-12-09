# -*- coding:utf-8 -*-
"""
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
"""

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        left, right = 0, len(array)-1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return "true"
            if array[mid] < target:
                left = mid + 1
            if array[mid] > target:
                right = mid - 1
        return "false"

while True:
    try:
        solution = Solution()
        inp = list(eval(raw_input()))
        target = inp[0]
        matrix = inp[1]
        
        if len(matrix[0]) == 0:
            print("false")
            continue
            
        n = 0
        for array in matrix:
            if array[0] <= target and array[-1] >= target:
                res = solution.Find(target, array)
                if res == "true":
                    print(res)
                    n += 1
                    break
        if not n:
            print("false")
                
    except:
        break