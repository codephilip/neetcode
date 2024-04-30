class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        empty = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in empty:
                return [empty[complement], i]
            empty[num] = i
