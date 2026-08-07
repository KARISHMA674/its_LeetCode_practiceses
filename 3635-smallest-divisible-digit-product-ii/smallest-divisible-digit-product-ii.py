class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        
        temp_t = t
        prime_counts = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                prime_counts[p] += 1
                temp_t //= p
        
        if temp_t > 1:
            return "-1"

        def get_min_digits(counts):
            """Returns the shortest/smallest string of digits needed to satisfy required prime counts."""
            c2, c3, c5, c7 = counts[2], counts[3], counts[5], counts[7]
            
            n9 = c3 // 2
            c3 %= 2
            
            n8 = c2 // 3
            c2 %= 3
            
            n4 = c2 // 2
            c2 %= 2
            
            n6 = 0
            n2 = c2
            if c2 == 1 and c3 == 1:
                n6, n2, c3 = 1, 0, 0
            elif n4 == 1 and c3 == 1:
                n4, n2, n6, c3 = 0, 1, 1, 0
            
            digits = []
            digits.extend(['2'] * n2)
            digits.extend(['3'] * c3)
            digits.extend(['4'] * n4)
            digits.extend(['5'] * c5)
            digits.extend(['6'] * n6)
            digits.extend(['7'] * c7)
            digits.extend(['8'] * n8)
            digits.extend(['9'] * n9)
            digits.sort()
            return "".join(digits)

        def digit_factors(d):
            f = {2: 0, 3: 0, 5: 0, 7: 0}
            if d in (2, 4, 8, 6):
                if d == 2: f[2] += 1
                elif d == 4: f[2] += 2
                elif d == 8: f[2] += 3
                elif d == 6: f[2] += 1; f[3] += 1
            if d in (3, 9, 6):
                if d == 3: f[3] += 1
                elif d == 9: f[3] += 2
            if d == 5: f[5] += 1
            if d == 7: f[7] += 1
            return f

        n = len(num)
        prefix_factors = [{2: 0, 3: 0, 5: 0, 7: 0}]
        zero_pos = -1

        for i, ch in enumerate(num):
            d = int(ch)
            if d == 0:
                if zero_pos == -1:
                    zero_pos = i
                prefix_factors.append(dict(prefix_factors[-1]))
            else:
                curr = dict(prefix_factors[-1])
                df = digit_factors(d)
                for p in curr:
                    curr[p] += df[p]
                prefix_factors.append(curr)

        if zero_pos == -1:
            if all(prefix_factors[-1][p] >= prime_counts[p] for p in prime_counts):
                return num

        
        for i in range(n - 1, -1, -1):
            if zero_pos != -1 and i > zero_pos:
                continue  
            
            curr_digit = int(num[i])
            pref = prefix_factors[i]
            
            for next_digit in range(curr_digit + 1, 10):
                needed = {}
                df = digit_factors(next_digit)
                for p in prime_counts:
                    needed[p] = max(0, prime_counts[p] - pref[p] - df[p])
                
                min_suffix = get_min_digits(needed)
                space = n - 1 - i
                
                if len(min_suffix) <= space:
                    ones = '1' * (space - len(min_suffix))
                    return num[:i] + str(next_digit) + ones + min_suffix

        min_suffix = get_min_digits(prime_counts)
        total_len = max(n + 1, len(min_suffix))
        ones = '1' * (total_len - len(min_suffix))
        return ones + min_suffix
        