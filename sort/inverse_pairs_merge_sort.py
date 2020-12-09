"""
逆序对个数问题，归并排序，O(NlogN)
"""
def inversePairs(arr, left, right):
    if left == right:
        return 0
    mid = left + (right - left) // 2
    left_pairs = inversePairs(arr, left, mid)
    right_pairs = inversePairs(arr, mid+1, right)
    merge_pairs = mergePairs(arr, left, mid, right)
    return left_pairs + right_pairs + merge_pairs

def mergePairs(arr, left, mid, right):
    l = left
    r = mid+1
    pairs = 0
    new_arr = []
    while l <= mid and r <= right:
        if arr[l] > arr[r]:
            pairs += (right - r + 1)
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
    print(arr)
    return pairs

# Test
arr = [5, 1, 9, 3, 7, 4, 8, 6, 2]
print(inversePairs(arr, 0, len(arr)-1))