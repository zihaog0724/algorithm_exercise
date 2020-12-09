"""
输入整型数组和排序标识，对其元素按照升序或降序进行排序

第一行输入数组元素个数
第二行输入待排序的数组，每个数用空格隔开
第三行输入一个整数0或1。0代表升序排序，1代表降序排序
"""
def mergeSort(arr, mode):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    arr_left = mergeSort(arr[:mid], mode)
    arr_right = mergeSort(arr[mid:], mode)
    if mode == 0:
        return mergeAscending(arr_left, arr_right)
    if mode == 1:
        return mergeDescending(arr_left, arr_right)

def mergeAscending(arr1, arr2):
    l, r = 0, 0
    new_arr = []
    while l < len(arr1) and r < len(arr2):
        if arr1[l] <= arr2[r]:
            new_arr.append(arr1[l])
            l += 1
        else:
            new_arr.append(arr2[r])
            r += 1

    while l < len(arr1):
        new_arr.append(arr1[l])
        l += 1

    while r < len(arr2):
        new_arr.append(arr2[r])
        r += 1

    return new_arr

def mergeDescending(arr1, arr2):
    l, r = 0, 0
    new_arr = []
    while l < len(arr1) and r < len(arr2):
        if arr1[l] >= arr2[r]:
            new_arr.append(arr1[l])
            l += 1
        else:
            new_arr.append(arr2[r])
            r += 1

    while l < len(arr1):
        new_arr.append(arr1[l])
        l += 1

    while r < len(arr2):
        new_arr.append(arr2[r])
        r += 1

    return new_arr

while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        mode = int(input())
        res = mergeSort(arr, mode)
        print(" ".join(map(str, res)))
    except:
        break