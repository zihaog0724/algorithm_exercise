# leetcode 3. isPalindrome

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        string_reverse = str(x)[::-1]
        return string == string_reverse

