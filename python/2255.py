class Solution:
    ## https://leetcode.com/problems/count-prefixes-of-a-given-string/
    def countPrefixes(self, words, s):
        return sum(map(s.startswith, words))
