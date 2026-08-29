from collections import deque


class Solution(object):

  def lexicographicallySmallestArray(self, nums, limit):
    """
    :type nums: List[int]
    :type limit: int
    :rtype: List[int]
    """
    sorted_nums = sorted(nums)

    num_to_group = {}
    group_to_list = []

    group_idx = 0
    group_to_list.append(deque([sorted_nums[0]]))
    num_to_group[sorted_nums[0]] = group_idx

    for i in range(1, len(sorted_nums)):
      if sorted_nums[i] - sorted_nums[i - 1] > limit:
        group_idx += 1
        group_to_list.append(deque())

      num_to_group[sorted_nums[i]] = group_idx
      group_to_list[group_idx].append(sorted_nums[i])

    res = []
    for num in nums:
      grp = num_to_group[num]
      res.append(group_to_list[grp].popleft())

    return res