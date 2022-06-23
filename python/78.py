class Solution:
 # https://leetcode.com/problems/subsets/
    def subsets(self, nums):
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output
        
