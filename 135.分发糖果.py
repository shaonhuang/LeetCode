#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans=[1 for i in range(len(ratings))]
        for i in range(len(ratings)-1):
            if ratings[i+1]>ratings[i] :
                ans[i+1]=ans[i]+1
        for i in range(1,len(ratings)):
            if ratings[-i-1]>ratings[-i] and ans[-i-1]<=ans[-i]:
                ans[-i-1]=ans[-i]+1

        return sum(ans)            
# @lc code=end

