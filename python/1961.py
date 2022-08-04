class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
	## https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/
	i = 0
        for word in words: 
            if s[i:i+len(word)] != word: return False 
            i += len(word)
            if i == len(s): return True 
        return False 
