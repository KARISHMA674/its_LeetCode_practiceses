class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        pair = {}
        stack = []

        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        
        res = []
        i = 0
        step = 1

        while i < n:
            if s[i] in '()':
                i = pair[i]
                step = -step
            else:
                res.append(s[i])
            i += step

        return "".join(res)