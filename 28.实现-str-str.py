#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            lenHaystack=len(list(haystack))
            lenNeedle=len(list(needle))
            for i in range(lenHaystack-lenNeedle+1):
                if haystack[i:i+lenNeedle]==needle:
                    return i
            return 0
        else: 
            return -1
# @lc code=end

