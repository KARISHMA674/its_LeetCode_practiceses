from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
            
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        s_len = len(s)
        
        if s_len < total_len:
            return []
            
        word_freq = Counter(words)
        res = []
        
        for i in range(word_len):
            left = i
            right = i
            seen = {}
            count = 0
            
            while right + word_len <= s_len:
               
                word = s[right : right + word_len]
                right += word_len
                
                if word in word_freq:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1
                    
                  
                    while seen[word] > word_freq[word]:
                        left_word = s[left : left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                        
                    
                    if count == word_count:
                        res.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = right
                    
        return res
        