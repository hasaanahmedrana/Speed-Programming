class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        n = 0
        for i in range(len(nums) - 1):
            if abs(nums[i + 1] - nums[i]) > n:
                n = abs(nums[i + 1] - nums[i])
        return n


