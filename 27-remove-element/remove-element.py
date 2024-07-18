class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pointer = 0
        for n in nums:
            if n != val:
                nums[pointer] = n
                pointer += 1
        return pointer
        
        
        