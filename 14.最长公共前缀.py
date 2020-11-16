#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 123/123 cases passed (28 ms)
        # Your runtime beats 99.49 % of python3 submissions
        # Your memory usage beats 7.21 % of python3 submissions (13.6 MB)
        ans = ''
        i = 0
        if len(strs) <= 1:
            if len(strs) == 0:
                return ''
            if len(strs) == 1:
                return strs[0]
        minLength = min(len(i) for i in strs)
        strsAllChars = [list(i) for i in strs]
        while i <= minLength-1 and minLength != 0:
            ToFSpace = []
            char = strsAllChars[0][i]
            for j in range(len(strs)):
                if char == strsAllChars[j][i]:
                    ToFSpace.append(True)
                else:
                    ToFSpace.append(False)
            continueOrNot = True
            for tmp in ToFSpace:
                if tmp == False:
                    continueOrNot = False
            if continueOrNot == True:
                ans += char
                i += 1
            else:
                break
        return ans


# @lc code=end
