class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        char_count=defaultdict(int)
        left=0
        max_len=0

        for right, ch in enumerate(s):
            char_count[ch]+=1

            while char_count[ch]>2:
                char_count[s[left]]-=1
                left+=1

            max_len=max(max_len, right-left+1)   


        return max_len    