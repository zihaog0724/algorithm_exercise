class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k < 1:
            return []
        k_arr = tinput[:k]
        k_maxheap = self.maxHeap(k_arr)
        for i in range(k, len(tinput)):
            if tinput[i] < k_maxheap[0]:
                k_maxheap[0] = tinput[i]
                k_maxheap = self.maxHeap(k_maxheap)
        return sorted(k_maxheap)
            
    def maxHeap(self, arr):
        """
        将给定数组转换为大根堆
        """
#        for i in range(len(arr)):
#            if i == 0:
#                continue

        for k in range(1, len(arr)):
            j = k
            while j > 0:
                father = j // 2
                if arr[j] > arr[father]:
                    tmp = arr[father]
                    arr[father] = arr[j]
                    arr[j] = tmp
                    j = father
                else:
                    break
        return arr

# Test
solution = Solution()
arr = [4,5,1,6,2,7,3,8]
k = 4
print(solution.GetLeastNumbers_Solution(arr, k))
