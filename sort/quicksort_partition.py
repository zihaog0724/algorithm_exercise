def quicksort(arr, left, right):
    if left >= right:
        return
    less, more = partition(arr, left, right)
    left_arr = quicksort(arr, left, less-1)
    right_arr = quicksort(arr, more+1, right)

def partition(arr, left, right):
    pivot = arr[right]
    less, more = left-1, right+1
    cur = left
    while cur < more:
        if arr[cur] < pivot:
            tmp = arr[less+1]
            arr[less+1] = arr[cur]
            arr[cur] = tmp
            less += 1
            cur += 1
        elif arr[cur] == pivot:
            cur += 1
        else:
            tmp = arr[more-1]
            arr[more-1] = arr[cur]
            arr[cur] = tmp
            more -= 1
    return less+1, more-1

arr = [4, 3, 2, 1, 0, 0, 4, 7, 1, 4, 4 ,8, 9]
quicksort(arr, 0, len(arr)-1)
print(arr)