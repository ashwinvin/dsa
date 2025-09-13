# https://leetcode.com/problems/merge-strings-alternately/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ""
        for a, b in zip(word1, word2):
            final += a + b

        if len(word1) < len(word2):
            final += word2[len(word1) :]
        elif len(word1) > len(word2):
            final += word1[len(word2) :]

        return final
