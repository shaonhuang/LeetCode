#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        listX = list(str(x))
        i = 0
        while listX[-(i+1)] == listX[i]:
            i += 1
            if i > len(listX)-1:
                break
        return True if i == len(listX) else False
# @lc code=end
