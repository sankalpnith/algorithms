#Given two strings text1 and text2, return the length of their longest common subsequence.
#A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.
#If there is no common subsequence, return 0.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        lcs = [[None]*(m+1) for i in range(n+1)] # n*m
        for i in range(n+1):
            for j in range(m+1):
                if i==0 or j==0:
                    lcs[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    lcs[i][j] = 1 + lcs[i-1][j-1]
                else:
                    lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
        return lcs[n][m]
