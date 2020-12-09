'''
查找和排序

题目：输入任意（用户，成绩）序列，可以获得成绩从高到低或从低到高的排列,相同成绩
都按先录入排列在前的规则处理。

示例：
jack      70
peter     96
Tom       70
smith     67

从高到低  成绩
peter     96
jack      70
Tom       70
smith     67

从低到高

smith     67
jack      70
Tom      70
peter     96

输入多行，先输入要排序的人的个数，然后输入排序方法0（降序）或者1（升序）再分别输入他们的名字和成绩，以一个空格隔开。
'''
while True: 
    try:
        num = int(input())
        mode = int(input())
        grade = []
        for i in range(num):
            grade.append(input().split())

        for i in range(1, num):
            j = i - 1
            while j >= 0:
                if mode: # ascending order
                    if int(grade[j+1][1]) < int(grade[j][1]):
                        tmp = grade[j]
                        grade[j] = grade[j+1]
                        grade[j+1] = tmp
                        j -= 1
                    else:
                        break

                else: #descending order
                    if int(grade[j+1][1]) > int(grade[j][1]):
                        tmp = grade[j]
                        grade[j] = grade[j+1]
                        grade[j+1] = tmp
                        j -= 1
                    else:
                        break

        for i in grade:
            print(i[0] + " " + i[1])
            
    except:
        break