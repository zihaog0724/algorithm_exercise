# hc100-lc 42. 接雨水


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        双指针解法题解见: https://zhuanlan.zhihu.com/p/556673613
        """
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        ret = 0
        while l < r:
            max_left = max(height[l], max_left)
            max_right = max(height[r], max_right)
            if max_left <= max_right:
                ret += (max_left - height[l])
                l += 1
            else:
                ret += (max_right - height[r])
                r -= 1
        return ret
