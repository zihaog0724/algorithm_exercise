# hot100-lc 239. 滑动窗口最大值

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0 or k == 0:
            return []
        if len(nums) == 1:
            return [nums[0]]

        queue = []
        ret = []
        for i in range(len(nums)):
            if len(queue) > 0 and i - k == queue[0]:
                queue.pop(0)

            while len(queue) > 0 and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

            if i >= k - 1:
                ret.append(nums[queue[0]])
        return ret
