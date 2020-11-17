#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # version 1
        # 91/91 cases passed (40 ms)
        # Your runtime beats 74.16 % of python3 submissions
        # Your memory usage beats 5.28 % of python3 submissions (13.7 MB)
        stack=[]
        data={
            '(':1,
            ')':1,
            '[':2,
            ']':2,
            '{':3,
            '}':3
        }
        if len(s)<=1:return False
        listStr=list(s)
        if ')' ==listStr[0]  or ']'==listStr[0] or '}' == listStr[0]:return False

        for c in listStr:
            
            if ')' != c and ']'!=c and '}' != c:
                stack.append(c)
            else:
                if stack!=[]:
                    if data[c] != data[stack[-1]]:
                        return False
                    else:
                        stack.pop()
                else:return False
        return True if stack==[] else False


        # version 2
        # 91/91 cases passed (64 ms)
        # Your runtime beats 7.32 % of python3 submissions
        # Your memory usage beats 5.28 % of python3 submissions (13.6 MB)

        # while '{}' in s or '()' in s or '[]' in s:
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        #     s = s.replace('()', '')
        # return s == ''


# @lc code=end

