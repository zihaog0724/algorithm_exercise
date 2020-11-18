#
# 二分查找
# @param n int整型 数组长度
# @param v int整型 查找值
# @param a int整型一维数组 有序数组
# @return int整型
#

class Solution:
    def upper_bound_(self,n,v,a):
        low, high = 0, n-1
        if v > a[n-1]:
            return n+1

        while low < high:
            mid = (low + high) // 2
            if v > a[mid]:
                low = mid+1
            else:
                high = mid

        return low+1

# Test
solution = Solution()
res = solution.upper_bound_(100,1,[2,3,4,4,4,7,7,8,10,10,11,12,13,14,15,15,17,18,19,23,24,24,24,24,25,26,26,26,27,27,28,29,29,30,33,36,38,38,40,40,41,43,43,43,44,46,46,47,51,52,52,53,54,56,57,57,57,58,58,61,61,61,62,64,64,66,66,67,67,67,70,72,74,74,74,75,75,78,78,78,79,79,80,83,83,83,83,84,84,86,88,89,89,90,91,91,92,93,93,96])
print(res)





        
