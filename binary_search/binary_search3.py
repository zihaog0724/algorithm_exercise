#
# 实现函数 int sqrt(int x).
# 计算并返回x的平方根
# @param x int整型
# @return int整型
#

class Solution:
    def sqrt(self , x ):
        # write code here
        if x <= 0:
            return 0
         
        low, high = 1, x
        while low <= high:
            mid = (low + high) // 2
            if mid**2 <= x and (mid+1)**2 > x:
                return mid
            if mid**2 < x:
                low = mid + 1
            if mid**2 > x:
                high = mid


solution = Solution()
print(solution.sqrt(16))
print(solution.sqrt(17))
print(solution.sqrt(25))
print(solution.sqrt(27))