# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例: 
#
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# Related Topics 堆 链表 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        length = len(lists)
        if length == 0:
            return ListNode(0).next
        if length == 1:
            return lists[0]
        left = lists[:length // 2]
        right = lists[length // 2:]
        if len(left) > 1:
            left = [self.mergeKLists(left)]
        if len(right) > 1:
            right = [self.mergeKLists(right)]
        left, right = left[0], right[0]
        if left is None:
            return right
        if right is None:
            return left
        if left.val <= right.val:
            result = ListNode(left.val)
            left = left.next
        else:
            result = ListNode(right.val)
            right = right.next
        result_temp = result
        while left is not None or right is not None:
            if left is None:
                result_temp.next = ListNode(right.val)
                right = right.next
            elif right is None:
                result_temp.next = ListNode(left.val)
                left = left.next
            elif left.val <= right.val:
                result_temp.next = ListNode(left.val)
                left = left.next
            else:
                result_temp.next = ListNode(right.val)
                right = right.next
            result_temp = result_temp.next
        result_temp.next = None
        return result

        # def mergeKLists(self, lists):
        #     """
        #     :type lists: List[ListNode]
        #     :rtype: ListNode
        #     """
        #     amount = len(lists)
        #     interval = 1
        #     while interval < amount:
        #         for i in range(0, amount - interval, interval * 2):
        #             lists[i] = self.merge2Lists(lists[i], lists[i + interval])
        #         interval *= 2
        #     return lists[0] if amount > 0 else lists
        #
        # def merge2Lists(self, l1, l2):
        #     head = point = ListNode(0)
        #     while l1 and l2:
        #         if l1.val <= l2.val:
        #             point.next = l1
        #             l1 = l1.next
        #         else:
        #             point.next = l2
        #             l2 = l1
        #             l1 = point.next.next
        #         point = point.next
        #     if not l1:
        #         point.next = l2
        #     else:
        #         point.next = l1
        #     return head.next

# leetcode submit region end(Prohibit modification and deletion)
