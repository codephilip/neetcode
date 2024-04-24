class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j + 1

        # I prefer the use of a set here as it shows better knowledge of data structs.
        # nums[:] = sorted(set(nums))
        # return len(nums)
