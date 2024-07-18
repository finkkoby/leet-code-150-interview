class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = 0
        for n in range(len(nums)):
            if nums[n] == val:
                nums[n] = '_'
                counter -= 1
        if counter < 0:
            nums.sort()
            return len(nums[slice(0, counter)])
        else:
            return len(nums)
        
        