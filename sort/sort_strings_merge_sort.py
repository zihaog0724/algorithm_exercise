"""
编写一个程序，将输入字符串中的字符按如下规则排序。

规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。

如，输入： Type 输出： epTy

规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。

如，输入： BabA 输出： aABb

规则 3 ：非英文字母的其它字符保持原来的位置。

如，输入： By?e 输出： Be?y
"""
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    arr_left = mergeSort(arr[:mid])
    arr_right = mergeSort(arr[mid:])
    return merge(arr_left, arr_right)

def merge(arr_left, arr_right):
    l, r = 0, 0
    new_arr = []
    while l < len(arr_left) and r < len(arr_right):
        if ord(arr_left[l].lower()) <= ord(arr_right[r].lower()):
            new_arr.append(arr_left[l])
            l += 1
        else:
            new_arr.append(arr_right[r])
            r += 1

    while l < len(arr_left):
        new_arr.append(arr_left[l])
        l += 1

    while r < len(arr_right):
        new_arr.append(arr_right[r])
        r += 1

    return new_arr


while True:
    try:
        strings = input()
        letters = []
        for i in strings:
            if i.isalpha():
                letters.append(i)
        sorted_letters = mergeSort(letters)

        res = []
        idx = 0
        for i in strings:
            if i.isalpha():
                res.append(sorted_letters[idx])
                idx += 1
            else:
                res.append(i)

        print("".join(res))

    except:
        break