class Solution:
    ## https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
    def minimumOperations(self, A):
        return len(set(A) - {0})
