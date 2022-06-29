class Solution:
    def containsDuplicate(self, nums):
        # https://leetcode.com/problems/contains-duplicate/
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
        
