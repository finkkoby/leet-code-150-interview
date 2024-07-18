class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tank = nums[0]
        if len(nums) > 1:
            if tank > 0:
                for n in nums[1:-1]:
                    tank -= 1
                    tank = max([tank, n])
                    if tank <= 0:
                        return False
                return tank > 0
            else:
                return False
        else:
            return True

