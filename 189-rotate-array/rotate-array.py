class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while len(nums) < k:
            k -= len(nums)

        length = len(nums)
        nums += nums[0:length - k]

        del nums[0:length - k]
