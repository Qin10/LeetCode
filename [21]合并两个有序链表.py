# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例： 
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            result = ListNode(l1.val)
            l1 = l1.next
        else:
            result = ListNode(l2.val)
            l2 = l2.next
        result_temp = result
        while l1 is not None or l2 is not None:
            if l1 is None:
                result_temp.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None:
                result_temp.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val <= l2.val:
                result_temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                result_temp.next = ListNode(l2.val)
                l2 = l2.next
            result_temp = result_temp.next
        result_temp.next = None
        return result

    # def mergeTwoLists(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     if l1 is None:
    #         return l2
    #     elif l2 is None:
    #         return l1
    #     elif l1.val < l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2
# leetcode submit region end(Prohibit modification and deletion)
