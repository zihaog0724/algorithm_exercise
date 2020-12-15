"""
牛牛手里有N根木棒,分别编号为1~N,现在他从N根里想取出三根木棒，使得三根木棒构成一个三角形,
你能计算出牛牛有多少种取法吗?(考虑两种取法中使用的木棒编号有一个不一样就认为是不同的取法)。
"""
"""
输入描述:
首先输入一个正整数N，接下来的一行共有N个正整数表示每个木棒的长度。

N ≤ 50, 木棒的长度 ≤ 10000.

输出描述:
输出一个整数表示方法数。
示例1
输入
5
1 2 3 4 5
输出
3
"""

while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        count = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if arr[i] + arr[j] <= arr[k]:
                        break
                    else:
                        count += 1
        print(count)
    except:
        break

