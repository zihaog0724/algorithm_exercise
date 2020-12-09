"""
小和问题，归并排序，O(NlogN)
"""
def smallSum(arr, left, right):
    if left == right:
        return 0
    mid = left + (right - left) // 2
    left_sum = smallSum(arr, left, mid)
    right_sum = smallSum(arr, mid+1, right)
    merge_sum = mergeSum(arr, left, mid, right)
    return left_sum + right_sum + merge_sum

def mergeSum(arr, left, mid, right):
    l = left
    r = mid+1
    Sum = 0
    new_arr = []
    while l <= mid and r <= right:
        if arr[l] < arr[r]:
            Sum += arr[l] * (right - r + 1)
            new_arr.append(arr[l])
            l += 1
        else:
            new_arr.append(arr[r])
            r += 1

    while l <= mid:
        new_arr.append(arr[l])
        l += 1

    while r <= right:
        new_arr.append(arr[r])
        r += 1

    for i in range(len(new_arr)):
        arr[left+i] = new_arr[i]
        
    return Sum

# Test
arr = [1, 3, 4, 2, 5]
print(smallSum(arr, 0, len(arr)-1))