# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。 
#
# 示例 1: 
#
# 输入: [1,3,5,6], 5
# 输出: 2
# 
#
# 示例 2: 
#
# 输入: [1,3,5,6], 2
# 输出: 1
# 
#
# 示例 3: 
#
# 输入: [1,3,5,6], 7
# 输出: 4
# 
#
# 示例 4: 
#
# 输入: [1,3,5,6], 0
# 输出: 0
# 
# Related Topics 数组 二分查找



# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head = 0
        last = len(nums) - 1
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        while head <= last:
            if last == head:
                if target > nums[head]:
                    return head + 1
                else:
                    return head
            mid = (head + last) // 2
            if target == nums[mid]:
                return mid
            if last - head == 1:
                if target < nums[head]:
                    return head
                elif target > nums[last]:
                    return last + 1
                else:
                    return last
            if target > nums[mid]:
                head = mid + 1
            else:
                last = mid - 1

# leetcode submit region end(Prohibit modification and deletion)
