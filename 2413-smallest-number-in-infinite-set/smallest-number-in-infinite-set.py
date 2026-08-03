import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.current = 1
        self.added_heap = []
        self.added_set = set()

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.added_heap:
            smallest = heapq.heappop(self.added_heap)
            self.added_set.remove(smallest)
            return smallest
        
        smallest = self.current
        self.current += 1
        return smallest

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
       
        if num < self.current and num not in self.added_set:
            heapq.heappush(self.added_heap, num)
            self.added_set.add(num)