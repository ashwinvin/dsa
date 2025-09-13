# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for el in t:
            if len(s) > i and s[i] == el:
                i += 1
        return True if len(s) == i else False
