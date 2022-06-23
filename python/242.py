class Solution:
# https://leetcode.com/problems/valid-anagram/x
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
        
