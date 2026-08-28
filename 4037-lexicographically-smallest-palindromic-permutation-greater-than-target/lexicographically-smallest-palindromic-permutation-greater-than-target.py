from collections import Counter


class Solution(object):

    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        cnt = Counter(s)

        odd_chars = [ch for ch, c in cnt.items() if c % 2 != 0]
        if (n % 2 == 0 and len(odd_chars) != 0) or (
            n % 2 == 1 and len(odd_chars) != 1
        ):
            return ""

        mid_char = odd_chars[0] if odd_chars else ""

        half_cnt = {ch: cnt[ch] // 2 for ch in cnt}
        m = n // 2

        
        temp_cnt = dict(half_cnt)
        possible_prefix = True
        for i in range(m):
            t_ch = target[i]
            if temp_cnt.get(t_ch, 0) > 0:
                temp_cnt[t_ch] -= 1
            else:
                possible_prefix = False
                break

        if possible_prefix:
            first_half = target[:m]
            cand = first_half + mid_char + first_half[::-1]
            if cand > target:
                return cand

        
        for i in range(m - 1, -1, -1):
            
            cur_cnt = dict(half_cnt)
            valid_prefix = True
            for j in range(i):
                ch = target[j]
                if cur_cnt.get(ch, 0) > 0:
                    cur_cnt[ch] -= 1
                else:
                    valid_prefix = False
                    break

            if not valid_prefix:
                continue

         
            for o in range(ord(target[i]) + 1, ord("z") + 1):
                c = chr(o)
                if cur_cnt.get(c, 0) > 0:
                    cur_cnt[c] -= 1
                    first_half = list(target[:i]) + [c]

                    
                    for ch_code in range(ord("a"), ord("z") + 1):
                        ch_str = chr(ch_code)
                        if cur_cnt.get(ch_str, 0) > 0:
                            first_half.extend([ch_str] * cur_cnt[ch_str])

                    first_half_str = "".join(first_half)
                    return first_half_str + mid_char + first_half_str[::-1]

        return ""