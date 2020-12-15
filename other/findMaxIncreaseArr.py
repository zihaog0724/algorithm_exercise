"""
牛牛现在有一个n个数组成的数列,牛牛现在想取一个连续的子序列,
并且这个子序列还必须得满足:最多只改变一个数,就可以使得这个连续的子序列是一个严格上升的子序列,
牛牛想知道这个连续子序列最长的长度是多少。
"""
"""
输出描述:
输出一个整数,表示最长的长度。
示例1
输入
6 
7 2 3 1 5 6
输出
5
"""

n = int(input())
arr = list(map(int, input().split()))
n = 6
arr = [7, 2, 3, 4, 5, 6]
head = [1] * n
for i in range(n-2, -1, -1):
    if arr[i+1] > arr[i]:
        head[i] = head[i+1] + 1

tail = [1] * n
for i in range(1, n):
    if arr[i] > arr[i-1]:
        tail[i] = tail[i-1] + 1

res = 1
for i in range(1, n-1):
    res = max(head[i], tail[i], res)
    if arr[i+1] - arr[i-1] >= 2:
        res = max(res, head[i+1]+tail[i-1]+1)
print(res)
