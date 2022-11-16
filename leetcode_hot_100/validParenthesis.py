# hot100-lc 20. validParenthesis


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        栈解法:
        先做个hashmap, 把三种括号对应起来
        只要分类讨论清楚何时压栈何时出栈即可
        压栈三种情况:
        (1) 栈为空
        (2) 栈顶元素不在map.keys()里, 说明栈顶是右括号, 肯定不能被消掉, 压栈
        (3) 栈顶元素在map.keys()里, 说明是左括号, 但新来的元素不是其对应的右括号, 消不掉, 压栈
        出栈只有一种情况:
        (1) 栈顶元素在map.keys()里, 说明是左括号, 且新来的元素恰好是其对应的右括号, 说明合法, 可以消掉, 出栈
        """
        mp = {'(': ')',
              '[': ']',
              '{': '}'}

        stack = []
        for char in s:
            if len(stack) == 0 or stack[-1] not in mp.keys():
                stack.append(char)
                continue
            if char != mp[stack[-1]]:
                stack.append(char)
                continue
            else:
                stack.pop()
        return len(stack) == 0
