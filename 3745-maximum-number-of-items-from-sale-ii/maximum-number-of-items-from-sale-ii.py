from collections import Counter


class Solution(object):

  def maximumSaleItems(self, items, budget):
    """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
    n = len(items)
    if n == 0 or budget == 0:
      return 0

    min_price = min(p for _, p in items)
    max_factor = max(f for f, _ in items)

    freq = Counter(f for f, _ in items)

    multiples = [0] * (max_factor + 1)
    for x in range(1, max_factor + 1):
      for m in range(x, max_factor + 1, x):
        if m in freq:
          multiples[x] += freq[m]

    
    pairs = []
    for f, p in items:
      deg = multiples[f] - 1  
      if deg > 0:
        pairs.append((p, deg))

    pairs.sort()

    ans = budget // min_price

    spent = 0
    items_so_far = 0

    for p, deg in pairs:
      if spent + p > budget:
        break

      can_buy = min(deg, (budget - spent) // p)

      rem_after_all = budget - (spent + can_buy * p)
      ans = max(
          ans, items_so_far + 2 * can_buy + (rem_after_all // min_price)
      )

      if can_buy >= 1:
        rem_after_less = budget - (spent + (can_buy - 1) * p)
        ans = max(
            ans,
            items_so_far + 2 * (can_buy - 1) + (rem_after_less // min_price),
        )

      if can_buy < deg:
        break

      spent += deg * p
      items_so_far += 2 * deg

    return ans