#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # version 1
        # 3999/3999 cases passed (52 ms)
        # Your runtime beats 91.66 % of python3 submissions
        # Your memory usage beats 5.8 % of python3 submissions (13.6 MB)
        # data = {
        #     'I': 1,
        #     'V': 5,
        #     'X': 10,
        #     'L': 50,
        #     'C': 100,
        #     'D': 500,
        #     'M': 1000
        # }
        # strLists = list(s)
        # num = 0
        # for i in strLists:
        #     num = data[i]+num
        # if 'CM' in s:
        #     num = num-200
        # if 'CD' in s:
        #     num = num-200
        # if 'XC' in s:
        #     num = num-20
        # if 'XL' in s:
        #     num = num-20
        # if 'IX' in s:
        #     num = num-2
        # if 'IV' in s:
        #     num = num-2
        # return num if num <=3999 else 0

        # version 2
        # 3999/3999 cases passed (60 ms)
        # Your runtime beats 68.5 % of python3 submissions
        # Your memory usage beats 6.37 % of python3 submissions (13.6 MB)
        data = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        def recursive_search(s: list, data, base):
            if len(s) >= 2:
                if data[s[0]] < data[s[1]]:
                    base = base - data[s[0]]*2

            base += data[s[0]]
            if len(s) == 1:
                return base
            s.pop(0)
            return recursive_search(s, data, base)

        return recursive_search(list(s), data,base=0)
        # @lc code=end
