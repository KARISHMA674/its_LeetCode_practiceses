class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        num = 0
        sign = 1  

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in '+-':
                res += sign * num
                num = 0
                sign = 1 if ch == '+' else -1
            elif ch == '(':
                
                stack.append(res)
                stack.append(sign)
                
                res = 0
                sign = 1
            elif ch == ')':
                res += sign * num
                num = 0
                
                res *= stack.pop()
                
                res += stack.pop()

        res += sign * num
        return res