from collections import defaultdict

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        row_masks = defaultdict(int)

        
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                row_masks[row] |= (1 << (col - 2))

        
        max_families = (n - len(row_masks)) * 2

        LEFT_MASK = 0b00001111   
        RIGHT_MASK = 0b11110000  
        MID_MASK = 0b00111100    

        for mask in row_masks.values():
            left_ok = not (mask & LEFT_MASK)
            right_ok = not (mask & RIGHT_MASK)
            mid_ok = not (mask & MID_MASK)

            if left_ok and right_ok:
                max_families += 2
            elif left_ok or right_ok or mid_ok:
                max_families += 1

        return max_families
        