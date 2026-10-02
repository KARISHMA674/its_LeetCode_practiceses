class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(boxGrid)
        n = len(boxGrid[0])
        
        for row in boxGrid:
        
            empty_pos = n - 1
            
            for col in range(n - 1, -1, -1):
                if row[col] == '*':
                   
                    empty_pos = col - 1
                elif row[col] == '#':
                    
                    row[col] = '.'
                    row[empty_pos] = '#'
                    empty_pos -= 1
        
        
        rotated = [['.'] * m for _ in range(n)]
        for r in range(m):
            for c in range(n):
                rotated[c][m - 1 - r] = boxGrid[r][c]
                
        return rotated