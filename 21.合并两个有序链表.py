#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # version 1
        # 208/208 cases passed (60 ms)
        # Your runtime beats 10.62 % of python3 submissions
        # Your memory usage beats 14.78 % of python3 submissions (13.5 MB)
        re = ListNode(0)
        r=re
        carry=0
        while(l1 or l2):
            x= l1.val if l1 else 999
            y= l2.val if l2 else 999
            if x<=y:
                carry=x
                if(l1!=None):l1=l1.next
            else:
                carry=y
                if(l2!=None):l2=l2.next
            r.next=ListNode(carry)
            r=r.next
        return re.next
# @lc code=end

