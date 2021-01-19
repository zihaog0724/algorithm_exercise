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






