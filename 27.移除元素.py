#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        for i in range(l-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)
# @lc code=end
