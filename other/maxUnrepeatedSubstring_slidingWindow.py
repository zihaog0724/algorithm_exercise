n = int(raw_input())
arr = list(map(int, raw_input().split()))

res = 1
left = 0
dic = {}
for i in range(n):
    if arr[i] in dic and left <= dic[arr[i]]:
        res = max(res, i - left)
        left = dic[arr[i]] + 1
    dic[arr[i]] = i
res = max(res, n - left)
print(res)