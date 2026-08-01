from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
       
        visited = set([0])
       
        queue = deque([0])
        
        while queue:
            current_room = queue.popleft()
            
           
            for key in rooms[current_room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
                    
       
        return len(visited) == len(rooms)