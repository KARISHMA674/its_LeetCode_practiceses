class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        ans = 0
        last_end = -1  
        for center in range(2 * n - 1):
            left = center // 2
            right = left + (center % 2)

            while left >= 0 and right < n and s[left] == s[right]:
                
                if left <= last_end:
                    break
                
                curr_len = right - left + 1
                if curr_len >= k:
                    
                    ans += 1
                    last_end = right
                    break
                
                left -= 1
                right += 1

        return ans