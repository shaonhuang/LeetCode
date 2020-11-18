#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        #version 1-0 runtime error idea is simple enough
        # listStr = list(s)
        # maxSubString = []
        # def isPalindromicString(str: list) -> bool:
        #     if len(str) > 1:
        #         for i in range(len(str)):
        #             if str[i] != str[-i-1]:
        #                 return False
        #     return True
        # for i in range(len(listStr)):
        #     for j in range(i, len(listStr)+1):
        #         if isPalindromicString(listStr[i:j]):
        #             if len(listStr[i:j]) > len(maxSubString):
        #                 maxSubString = listStr[i:j]
        # return ''.join(maxSubString)

        # version 2
        # 176/176 cases passed (9768 ms)
        # Your runtime beats 5.01 % of python3 submissions
        # Your memory usage beats 55.49 % of python3 submissions (13.6 MB)
        for j in range(len(s), -1, -1):
            for i in range(len(s)-j, -1, -1):
                if (s[i:i+j]) == s[i:i+j][::-1]:
                    return s[i:i+j][::-1]


# @lc code=end
