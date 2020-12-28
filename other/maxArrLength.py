"""
给定一个数组arr，返回arr的最长无的重复子串的长度(无重复指的是所有数字都不相同)。
"""

class Solution:
    def maxLength(self , arr):
        # write code here
        dic = {}
        res = 1
        j = -1
        for i, val in enumerate(arr):
            if val in dic and dic[val] > j:
                j = dic[val]
                dic[val] = i
            else:
                dic[val] = i
                res = max(res, i-j)
        return res

solution = Solution()
arr = [4,3,1,5,6,8,9,5,4,3,2]
print(solution.maxLength(arr))
