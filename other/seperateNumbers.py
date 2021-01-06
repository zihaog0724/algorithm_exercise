'''
将整数n分成k份，且每份不能为空，任意两个方案不能相同(不考虑顺序)。
例如：n=7，k=3，下面三种分法被认为是相同的。
1，1，5; 
1，5，1; 
5，1，1;
问有多少种不同的分法。
输入：n，k ( 6 < n ≤ 200，2 ≤ k ≤ 6 )
输出：一个整数，即不同的分法。
'''

def process(n, k, already_sum, step, pre):
    global res
    if step == k:
        if already_sum == n:
            res += 1
        else:
            return

    for i in range(pre, n-already_sum+1):
        process(n, k, already_sum+i, step+1, i)

res = 0
process(7, 3, 0, 0, 1)
print(res)
