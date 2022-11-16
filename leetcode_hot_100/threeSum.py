# hot100-lc 15. threeSum


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        双指针法思路:
        先做个排序, 然后遍历数组, 当前数nums[i]作为anchor, 两个指针分别为i+1和len(nums)-1, 记为l和r
        大体思路为, 如果sum=anchor+nums[l]+nums[r]大于0, 说明这个sum大了, r指针左移让sum变小寻找答案
        相反如果sum=anchor+nums[l]+nums[r]小于0, 说明这个sum小了, l指针右移让sum变大寻找答案
        因为题目要求答案之间互相不能重复, 所以要在遍历及指针移动过程中去重, 具体为
        如果nums[i]=nums[i-1], 说明这次的anchor和上次一样, 直接跳过
        如果sum=anchor+nums[l]+nums[r]=0, 按理说应该l+=1 and r-=1继续寻找
        但加入排序后数组为[-2, 0, 0, 2, 2]这种情况, 发现在找到[-2, 0, 2]答案后, l和r指针移动, 下一个答案就重复了,
        因此对这种情况也要去重
        """
        if len(nums) < 3:
            return []

        self.qsort(nums, 0, len(nums) - 1)
        ret = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            anchor = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if (anchor + nums[l] + nums[r]) > 0:
                    r -= 1
                elif (anchor + nums[l] + nums[r]) < 0:
                    l += 1
                else:
                    ret.append([anchor, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return ret

    def qsort(self, nums, left, right):
        if left >= right:
            return
        less, more = self.partition(nums, left, right)
        self.qsort(nums, left, less)
        self.qsort(nums, more, right)

    def partition(self, nums, left, right):
        less, cur, more = left - 1, left, right + 1
        pivot = nums[right]
        while cur < more:
            if nums[cur] < pivot:
                tmp = nums[less + 1]
                nums[less + 1] = nums[cur]
                nums[cur] = tmp
                less += 1
                cur += 1
            elif nums[cur] == pivot:
                cur += 1
            else:
                tmp = nums[more - 1]
                nums[more - 1] = nums[cur]
                nums[cur] = tmp
                more -= 1
        return less, more
