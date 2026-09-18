class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
       
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        valid_intervals = []

     
        for ch in set(s):
            start = first[ch]
            end = last[ch]
            is_valid = True

            i = start
            while i <= end:
                cur = s[i]
              
                if first[cur] < start:
                    is_valid = False
                    break
                end = max(end, last[cur])
                i += 1

            if is_valid:
                valid_intervals.append((end, start))

        valid_intervals.sort()

        res = []
        prev_end = -1
        for end, start in valid_intervals:
            if start > prev_end:
                res.append(s[start : end + 1])
                prev_end = end

        return res