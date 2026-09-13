from collections import defaultdict


class Solution(object):

  def largestOverlap(self, img1, img2):
    """
    :type img1: List[List[int]]
    :type img2: List[List[int]]
    :rtype: int
    """
    n = len(img1)

    points1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
    points2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

    shift_count = defaultdict(int)

    for r1, c1 in points1:
      for r2, c2 in points2:
        shift_vector = (r2 - r1, c2 - c1)
        shift_count[shift_vector] += 1

    return max(shift_count.values()) if shift_count else 0