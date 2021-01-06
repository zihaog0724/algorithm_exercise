#
# max sum of the subarray
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxsumofSubarray(self, arr):
        # write code here
        pre_sum = 0
        res = 0
        for i in arr:
            if pre_sum + i < 0:
                pre_sum = 0
            else:
                pre_sum += i
            res = max(res, pre_sum)
        return res