class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        def remove(s, i_start, j_start, open_p, close_p):
            count = 0
            for i in range(i_start, len(s)):
                if s[i] == open_p:
                    count += 1
                elif s[i] == close_p:
                    count -= 1
                
                
                if count < 0:
                    for j in range(j_start, i + 1):
                        
                        if s[j] == close_p and (j == j_start or s[j] != s[j - 1]):
                            remove(s[:j] + s[j+1:], i, j, open_p, close_p)
                    return

            
            reversed_s = s[::-1]
            if open_p == '(':
                remove(reversed_s, 0, 0, ')', '(')
            else:
                res.append(reversed_s)

        remove(s, 0, 0, '(', ')')
        return res