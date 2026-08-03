import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        head_heap = []
        tail_heap = []
        
        n = len(costs)
        left = 0
        right = n - 1
        
        while left < candidates and left <= right:
            heapq.heappush(head_heap, costs[left])
            left += 1
            
        while right >= n - candidates and left <= right:
            heapq.heappush(tail_heap, costs[right])
            right -= 1
            
        total_cost = 0
        
        for _ in range(k):
            if not tail_heap or (head_heap and head_heap[0] <= tail_heap[0]):
                total_cost += heapq.heappop(head_heap)
                if left <= right:
                    heapq.heappush(head_heap, costs[left])
                    left += 1
            else:
                total_cost += heapq.heappop(tail_heap)
                if left <= right:
                    heapq.heappush(tail_heap, costs[right])
                    right -= 1
                    
        return total_cost        