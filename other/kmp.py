class Solution:
    def get_next_arr(self, str2):
        if len(str2) == 1:
            return [-1]
        nex = [0] * len(str2)
        nex[0], nex[1] = -1, 0
        i = 2
        j = 0 
        while i < len(str2):
            if str2[i-1] == str2[j]:
                nex[i] = j + 1
                i += 1
                if i < len(str2):
                    j = nex[i-1]
            elif j > 0:
                j = nex[j]
            else:
                i += 1
                if i < len(str2):
                    j = nex[i-1]
                continue
        return nex

    def kmp(self, n, t):
        for i in range(2, 17):
            str1 = self.convert(n, i)
            str2 = t
            nex = self.get_next_arr(str2)
            x, y = 0, 0
            while x < len(str1) and y < len(str2):
                if str1[x] == str2[y]:
                    x += 1
                    y += 1
                elif nex[y] == -1:
                    x += 1
                else:
                    y = nex[y]
            if y == len(str2):
                return "yes"
        return "no"

    def convert(self, n, k):
        res = ""
        for i in range(1, n+1):
            remainder_list = []
            quotient = i
            while quotient > 0:
                remainder = quotient % k
                if remainder >= 10:
                    remainder = chr(65 + (remainder - 10))
                remainder_list.append(remainder)
                quotient = int(quotient / k)

            remainder_list.reverse()
            for j in remainder_list:
                res += str(j)
        return res

while True:
    try:
        n = int(raw_input())
        t = map(str, raw_input())
        solution = Solution()
        print(solution.kmp(n, t))
    except:
        break