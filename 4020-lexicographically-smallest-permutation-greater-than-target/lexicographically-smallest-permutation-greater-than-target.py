from collections import Counter

class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        s_count = Counter(s)
        
        
        prefix_counts = Counter()
        valid_prefix = [True] * (n + 1)
        
        for i in range(n):
            prefix_counts[target[i]] += 1
            if prefix_counts[target[i]] > s_count[target[i]]:
                for j in range(i + 1, n + 1):
                    valid_prefix[j] = False
                break
        
        
        for i in range(n - 1, -1, -1):
            if not valid_prefix[i]:
                continue
            
            
            rem_count = Counter(s)
            for j in range(i):
                rem_count[target[j]] -= 1
            
            
            target_char = target[i]
            best_c = None
            for char_code in range(ord(target_char) + 1, ord('z') + 1):
                c = chr(char_code)
                if rem_count[c] > 0:
                    best_c = c
                    break
            
            if best_c is not None:
                
                rem_count[best_c] -= 1
                
                suffix = []
                for char_code in range(ord('a'), ord('z') + 1):
                    c = chr(char_code)
                    if rem_count[c] > 0:
                        suffix.append(c * rem_count[c])
                
                return target[:i] + best_c + "".join(suffix)
        
        return ""
        