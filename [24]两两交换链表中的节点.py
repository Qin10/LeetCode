# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
#
# 
#
# 示例: 
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 
# Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        link = ListNode(0)
        link.next = head
        if link.next is None:
            return link.next
        fast = link.next
        slow = link
        while fast is not None and fast.next is not None:
            slow.next = fast.next
            fast.next = fast.next.next
            slow.next.next = fast
            slow = slow.next.next
            fast = fast.next
        return link.next
# leetcode submit region end(Prohibit modification and deletion)
