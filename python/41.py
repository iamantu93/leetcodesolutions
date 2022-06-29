class Solution:
    # https://leetcode.com/problems/first-missing-positive/
    def firstMissingPositive(self, nums):
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res += 1
        return res
