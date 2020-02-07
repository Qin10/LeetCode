# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1: 
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 
#
# 示例 2: 
#
# 输入: 1->1->1->2->3
# 输出: 2->3
# Related Topics 链表



# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = temp = ListNode(0)
        node.next = head
        num = None
        while temp and temp.next:
            if temp.next.val != num:
                num = temp.next.val
                if temp.next.next and temp.next.val == temp.next.next.val:
                    temp.next = temp.next.next.next
                else:
                    temp = temp.next
            else:
                temp.next = temp.next.next
        return node.next

# leetcode submit region end(Prohibit modification and deletion)
