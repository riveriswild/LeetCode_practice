"""
Given two strings s and t, return true if t is an anagram of s and false otherwise
"""


class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False

    #     countS, countT = {}, {}

    #     for i in range(len(s)):
    #         countS[s[i]] = countS.get(s[i], 0) + 1
    #         countT[t[i]] = countT.get(t[i], 0) + 1
    #     for c in countS:
    #         if countS[c]!= countT.get(c, 0):
    #             return False
    #     return True
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
