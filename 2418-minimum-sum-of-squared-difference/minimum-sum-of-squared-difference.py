class Solution(object):

  def minSumSquareDiff(self, nums1, nums2, k1, k2):
    """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
    k = k1 + k2
    diffs = [abs(a - b) for a, b in zip(nums1, nums2)]

    total_diff = sum(diffs)
    if total_diff <= k:
      return 0

    max_d = max(diffs)
    freq = [0] * (max_d + 1)
    for d in diffs:
      freq[d] += 1

    
    for v in range(max_d, 0, -1):
      if freq[v] == 0:
        continue

      if k >= freq[v]:
        
        k -= freq[v]
        freq[v - 1] += freq[v]
        freq[v] = 0
      else:
        
        freq[v - 1] += k
        freq[v] -= k
        k = 0
        break

    return sum(count * (v**2) for v, count in enumerate(freq))