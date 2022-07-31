class Solution:
    # https://leetcode.com/problems/count-and-say/
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                    for digit, group in itertools.groupby(s))
        return s
        
