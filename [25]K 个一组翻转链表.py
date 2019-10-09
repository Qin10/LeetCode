# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。 
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。 
#
# 示例 : 
#
# 给定这个链表：1->2->3->4->5 
#
# 当 k = 2 时，应当返回: 2->1->4->3->5 
#
# 当 k = 3 时，应当返回: 3->2->1->4->5 
#
# 说明 : 
#
# 
# 你的算法只能使用常数的额外空间。 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
# Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        link = ListNode(0)
        link.next = head
        if k == 1:
            return link.next
        length = 0
        temp = link.next
        while temp is not None:
            length += 1
            temp = temp.next
        fast = link.next
        slow = link
        for i in range(length // k):
            temp_list = []
            temp = fast
            for j in range(k + 1):
                temp_list.append(temp)
                if j != k:
                    temp = temp.next
            for j in range(k + 1):
                if j != k:
                    slow.next = temp_list[-j - 2]
                    slow = slow.next
                else:
                    slow.next = temp_list[-1]
                    fast = slow.next
        return link.next
# leetcode submit region end(Prohibit modification and deletion)
