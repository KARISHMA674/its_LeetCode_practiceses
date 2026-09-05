class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        ranges = []
        n= len(nums)
        i = 0

        while i < n:
            start = nums[i]

            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1

            end = nums[i]
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append("{}->{}".format(start, end))

            i += 1
        return ranges            