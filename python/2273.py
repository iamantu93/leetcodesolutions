class Solution:
    ## https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 0
        while i < len(words) - 1:
            if sorted(words[i]) == sorted(words[i + 1]):
                words.remove(words[i + 1])
                continue
            i += 1
        return words
