class Solution:
    # @param num, a list of integers
    # @return a string
# https://leetcode.com/problems/largest-number/
    def largestNumber(self, num):
        num = [str(x) for x in num]
        num.sort(cmp=lambda x, y: cmp(y+x, x+y))
        return ''.join(num).lstrip('0') or '0'
