class Solution(object):

  def resultArray(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    rem_counts = [0] * k

    current_rem = [0] * k

    for num in nums:
      r = num % k
      next_rem = [0] * k

      next_rem[r] += 1

     
      for prev_r in range(k):
        if current_rem[prev_r] > 0:
          next_r = (prev_r * r) % k
          next_rem[next_r] += current_rem[prev_r]

    
      for i in range(k):
        rem_counts[i] += next_rem[i]

      current_rem = next_rem

    return rem_counts