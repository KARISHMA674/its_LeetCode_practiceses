from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        R = len(classroom)
        C = len(classroom[0])
        
        start = None
        dirty_tiles = []
        
        for r in range(R):
            for c in range(C):
                char = classroom[r][c]
                if char == 'S':
                    start = (r, c)
                elif char == 'D' or char == 'L':  # 
                    dirty_tiles.append((r, c))
                    
        k = len(dirty_tiles)
        if k == 0:
            return 0
            
        dirty_map = {pos: i for i, pos in enumerate(dirty_tiles)}
        target_mask = (1 << k) - 1
        
        
        visited = {}
        
        sr, sc = start
        initial_mask = 0
        if (sr, sc) in dirty_map:
            initial_mask |= (1 << dirty_map[(sr, sc)])
            
        queue = deque([(sr, sc, initial_mask, energy, 0)])
        visited[(sr, sc, initial_mask)] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, cur_e, steps = queue.popleft()
            
            if mask == target_mask:
                return steps
            
            if cur_e == 0:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < R and 0 <= nc < C:
                    cell = classroom[nr][nc]
                    if cell == 'X' or cell == '#':
                        continue
                    
                    next_e = cur_e - 1
                    
                    if cell == 'R' or cell == 'C':
                        next_e = energy
                        
                    next_mask = mask
                    if (nr, nc) in dirty_map:
                        next_mask |= (1 << dirty_map[(nr, nc)])
                        
                    state_key = (nr, nc, next_mask)
                    
                 
                    if state_key not in visited or visited[state_key] < next_e:
                        visited[state_key] = next_e
                        queue.append((nr, nc, next_mask, next_e, steps + 1))
                        
        return -1