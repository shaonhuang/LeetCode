#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:

    # methods 1 complex way
    # def isUnique(self, s: str) -> bool:
    #     for char in s:
    #         if s.count(char) > 1:
    #             return False
    #         else:
    #             continue
    #     return True

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     i, j, Max = 0, 0, 0
    #     j += 1
    #     while j <= len(s):
    #         if self.isUnique(s[i:j]):
    #             Max = max(j-i, Max)
    #             j += 1
    #         else:
    #             i += 1
    #     return Max

    # improved
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        i, j, Max = 0, 0, 1
        j += 1
        while j < len(s):
            if s[j] in s[i:j]:
                tmpIndex = s[i:j].index(s[j])
                i = tmpIndex+i+1
                j += 1
            else:
                Max = max(j-i+1, Max)
                j += 1

        return Max

# @lc code=end
