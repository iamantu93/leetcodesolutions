class Solution(object):
# https://leetcode.com/problems/first-unique-character-in-a-string/
    def firstUniqChar(self, s):
        
        
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
        
