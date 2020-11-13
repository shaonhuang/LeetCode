#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)
        left = (m + n + 1)//2
        right = (m + n + 2)//2
        return (findKth(nums1, 0, nums2, 0, left)+findKth(nums1, 0, nums2, 0, right))/2
        def findKth(num1, i, nums2, j, k):
            if i >= len(nums1):
                return num2[j+k / 2 - 1]
            if j >= len(nums2):
                return num1[i+k / 2 - 1]
            if(k == 1):
                return min(nums1[i], nums2[j])
            midVal1 = nums1[i + k / 2 -1] if (i + k / 2 - 1 < nums1.length) else pow(10, 6)+1
            midVal2 = nums2[j + k / 2 -1] if (j + k / 2 - 1 < nums2.length) else pow(10, 6)+1
            if(midVal1 < midVal2):
                return findKth(nums1, i + k / 2, nums2, j, k - k / 2)
            else
                return findKth(nums1, i, nums2, j + k / 2, k - k / 2)



# @lc code=end
