#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f = 0
        s = 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        s = 0
        while s != f:
            f = nums[f]
            s = nums[s]
        return s
# @lc code=end
