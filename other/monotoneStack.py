'''
给定一个不含有重复值的数组 arr，找到每一个 i 位置左边和右边离 i 位置最近且值比 arr[i] 小的位置。返回所有位置相应的信息。


输入描述:
第一行输入一个数字 n，表示数组 arr 的长度。

以下一行输出 n个数字，表示数组的值。


输出描述:
输出n行，每行两个数字 L 和 R，如果不存在，则值为-1，下标从0开始。
示例1
输入
7
3 4 1 5 6 2 7
'''

arr = [3,4,1,5,6,2,7]
n = len(arr)
stack = [[[0], arr[0]]]
res = [[-1, -1] for i in range(n)]
for i in range(1, n):
    if arr[i] > stack[-1][-1]:
        stack.append([[i], arr[i]])
    elif arr[i] == stack[-1][-1]:
        stack[-1][0].append(i)
    else:
        while len(stack) > 0:
            if arr[i] < stack[-1][-1]:
                cur_res = stack.pop()
                for j in cur_res[0]:
                    res[j][1] = i 
                    if len(stack) > 0:
                        res[j][0] = stack[-1][0][-1]
            elif arr[i] == stack[-1][-1]:
                stack[-1][0].append(i)
                break
            else:
                stack.append([[i], arr[i]])
                break
        if len(stack) == 0:
            stack.append([[i], arr[i]])

while len(stack) > 0:
    cur_res = stack.pop()
    for i in cur_res[0]:
        if len(stack) > 0:
            res[i][0] = stack[-1][0][-1]

print(res)





