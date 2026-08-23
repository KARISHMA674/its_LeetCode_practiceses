class Solution:
    def sumGame(self, num):
        n = len(num)
        half = n // 2
        
        sum_diff = 0
        q_diff = 0
        
        for i in range(half):
            if num[i] == '?':
                q_diff += 1
            else:
                sum_diff += int(num[i])
                
        for i in range(half, n):
            if num[i] == '?':
                q_diff -= 1
            else:
                sum_diff -= int(num[i])
    
        if q_diff % 2 != 0:
            return True
       
        return sum_diff + (q_diff // 2) * 9 != 0
        