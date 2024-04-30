class Solution(object):
    def removeElement(self, nums, val):
        insertPosition = 0
        for num in nums:
            if num != val:
                nums[insertPosition] = num
                insertPosition += 1
        return insertPosition
