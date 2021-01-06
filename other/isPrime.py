'''
已知 n 个整数 x1,x2,…,xn，以及一个整数 k（k＜n）。
从 n 个整数中任选 k 个整数相加，可分别得到一系列的和。
例如当 n=4，k＝3，4 个整数分别为 3，7，12，19 时，可得全部的组合与它们的和为：
3＋7＋12=22　　3＋7＋19＝29　　7＋12＋19＝38　　3＋12＋19＝34。
现在，要求你计算出和为素数共有多少种。
例如上例，只有一种的和为素数：3＋7＋19＝29）。
'''

def isPrime(already_sum):
    for i in range(2, already_sum):
        if already_sum % i == 0:
            return False
    return True

def process(n, k, arr, index, step, already_sum):
    global res
    if step == k:
        if isPrime(already_sum):
            res += 1 
        return

    for i in range(index, n):
        process(n, k, arr, i+1, step+1, already_sum+arr[i])

while True:
    try:
        inp = list(map(int, raw_input().split(" ")))
        n = inp[0]
        k = inp[1]
        arr = list(map(int, raw_input().split(" ")))
        res = 0
        process(n, k, arr, 0, 0, 0)
        print(res)
    except:
        break

