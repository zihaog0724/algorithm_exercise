# hot100-lc 347. 前K个高频元素


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
        freq = list(dic.items())
        self.qsort(freq, 0, len(freq) - 1)
        ret = []
        for i in range(k):
            ret.append(freq[-(i + 1)][0])
        return ret

    def qsort(self, nums, left, right):
        if right <= left:
            return
        less, more = self.partition(nums, left, right)
        self.qsort(nums, left, less)
        self.qsort(nums, more, right)

    def partition(self, nums, left, right):
        pivot = nums[right][1]
        less, more = left - 1, right + 1
        cur = left
        while cur < more:
            if nums[cur][1] < pivot:
                tmp = nums[cur]
                nums[cur] = nums[less + 1]
                nums[less + 1] = tmp
                less += 1
                cur += 1
            elif nums[cur][1] == pivot:
                cur += 1
            else:
                tmp = nums[cur]
                nums[cur] = nums[more - 1]
                nums[more - 1] = tmp
                more -= 1
        return less, more
