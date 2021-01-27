'''
小A非常喜欢回文串，当然我们都知道回文串这种情况是非常特殊的。所以小A只想知道给定的一个字符串的最大回文子串是多少，但是小A对这个结果并不是非常满意。现在小A可以对这个字符串做一些改动，他可以把这个字符串最前面的某一段连续的字符(不改变顺序)移动到原先字符串的末尾。那么请问小A通过这样的操作之后(也可以选择不移动)能够得到最大回文子串的长度是多少。

输出描述:
一行输出一个整数，表示通过这样的操作后可以得到最大回文子串的长度。
示例1
输入
dcbaabc
输出
7
说明
将前面的dcba移动到末尾变成abcdcba，这个字符串的最大回文子串就是它本身，长度为7
'''

class Solution:
    def add_sharp(self, string):
        new_string = []
        for i in string:
            new_string.append("#")
            new_string.append(i)
        new_string.append("#")
        return new_string

    def manacher(self, string):
        if len(string) == 1:
            return 1
        string = self.add_sharp(string)
        R, C = 0, 0 # max right boundary & its center
        radius_arr = [1] * len(string)
        for i in range(1, len(string)):
            if i > R:
                R, C = i, i
                x = 1
                while (i-x) >= 0 and (i+x) < len(string):
                    if string[i-x] == string[i+x]:
                        R += 1
                        x += 1
                    else:
                        break
                radius_arr[i] = R - i + 1

            else: # i <= R
                L = C - (R - C)
                i_prime = C - (i - C)
                if i_prime > L:
                    radius_arr[i] = radius_arr[i_prime]
                elif i_prime < L:
                    radius_arr[i] = R - i + 1
                else: # i_prime = L
                    x = R - i + 1
                    while (i-x) >= 0 and (i+x) < len(string):
                        if string[i-x] == string[i+x]:
                            R += 1
                            x += 1
                        else:
                            break
                    radius_arr[i] = R - i + 1
        return max(radius_arr) - 1

while True:
    try:
        solution = Solution()
        string = raw_input()
        res = 0
        for i in range(1, len(string)):
            new_string = string[i:] + string[0:i]
            res = max(res, solution.manacher(new_string))
        print(res)
    except:
        break






