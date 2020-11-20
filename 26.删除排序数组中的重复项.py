#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        tmp = nums[0]
        i = 1
        while i <len(nums):
            if tmp == nums[i]:
                del nums[i]
            else:
                tmp = nums[i]
                i += 1
        return len(nums)
# @lc code=end
