#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        num=n
        num_str=[i for i in str(num)]
        isAppear=[]
        ans=0
        while ans!=1:
            ans=0
            for tmp in num_str:
                ans=ans+pow(int(tmp),2)
            if ans not in isAppear:
                isAppear.append(ans)
            else:
                return False
            num_str=[i for i in str(ans)]
        return True
# @lc code=end

