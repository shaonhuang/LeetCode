#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # version 1
        # return  (int(''.join(list(str(x))[::-1])) if x >= 0 else int(''.join(list(str(abs(x)))[::-1]))*(-1)) if -pow(2, 31) < (int(''.join(list(str(x))[::-1])) if x >= 0 else int(''.join(list(str(abs(x)))[::-1]))*(-1)) and  (int(''.join(list(str(x))[::-1])) if x >= 0 else int(''.join(list(str(abs(x)))[::-1]))*(-1)) < pow(2, 31) else 0

        # version 2
        # Your runtime beats 94.08 % of python3 submissions
        # Your memory usage beats 36.96 % of python3 submissions (13.4 MB)
        # num = (int(''.join(list(str(x))[::-1])) if x >=0 else int(''.join(list(str(abs(x)))[::-1]))*(-1))
        # num31 = pow(2, 31)
        # return num if -num31 < num and num < num31 else 0

        # version 3
        num = int(''.join(list(str(abs(x)))[::-1]))
        num = num if x >= 0 else -num
        num31 = pow(2, 31)
        return num if -num31 < num and num < num31 else 0

# @lc code=end
