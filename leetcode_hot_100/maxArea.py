# hot100-lc 11. 盛水最多的容器

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        双指针l, r:
        首先明确当前[l, r]之间的面积 cur_area = (r - l) * min(height[l], height[r])
        遍历完数组取最大就可以了, 因此重点是l和r两个指针如何移动
        左指针往右移动, 右指针往左移动, 根据木桶效应, 面积有较短的柱子决定
        因此, 若移动指向较高柱子的指针, 移动后围城的面积只会更小, 没有意义
        所以要移动较低柱子的指针
        """
        l, r = 0, len(height) - 1
        ret = 0
        while l < r:
            cur_area = (r - l) * min(height[l], height[r])
            if cur_area > ret:
                ret = cur_area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ret
