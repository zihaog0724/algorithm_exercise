# leetcode 7. reverse

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string = str(x)
        res_str = ""
        if string[0] == "-":
            res_str = "-" + string[-1:0:-1]
        else:
            res_str = string[-1::-1]
        return int(res_str) if -2147483648 < int(res_str) < 2147483648 else 0
