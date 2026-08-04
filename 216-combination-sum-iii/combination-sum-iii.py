class Solution(object):

  def combinationSum3(self, k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    if n > 45 or n < k:
      return []

    res = []

    def backtrack(start_num, current_path, current_sum):
      if len(current_path) == k:
        if current_sum == n:
          res.append(list(current_path))
        return

      if current_sum > n:
        return

  
      for num in range(start_num, 10):
        current_path.append(num)
        backtrack(num + 1, current_path, current_sum + num)
        current_path.pop() 

    backtrack(1, [], 0)
    return res
        