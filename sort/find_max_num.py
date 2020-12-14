# 给定一个数组由一些非负整数组成，
# 现需要将他们进行排列并拼接，使得最后的结果最大，返回值需要是string类型 否则可能会溢出
# [30, 1] → “301”

#
# 最大数
# @param nums int整型一维数组 
# @return string字符串
#


class Solution:
    def solve(self, nums):
        if sum(nums) == 0:
            return str(0)
        arr = [i for i in nums if i != 0]
        num_zeros = len(nums) - len(arr)
        sorted_arr = self.sort(arr)
        for i in range(num_zeros):
            sorted_arr.append(0)
        return "".join(map(str, sorted_arr))

    def sort(self, arr):
        for i in range(1, len(arr)):
            j = i - 1
            while j >= 0:
                if int(str(arr[j+1]) + str(arr[j])) > int(str(arr[j]) + str(arr[j+1])):
                    tmp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = tmp
                    j -= 1
                else:
                    break
        return arr

# Test
solution = Solution()
arr = [0, 0]
print(solution.solve(arr))