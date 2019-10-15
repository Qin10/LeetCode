# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
#
# 示例 1: 
#
# 输入: [1,2,0]
# 输出: 3
# 
#
# 示例 2: 
#
# 输入: [3,4,-1,1]
# 输出: 2
# 
#
# 示例 3: 
#
# 输入: [7,8,9,11,12]
# 输出: 1
# 
#
# 说明: 
#
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。 
# Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        dic = {}
        for i in nums:
            if i <= 0: continue
            if i not in dic: dic[i] = 1
        for i in range(1, len(nums) + 2):
            if not i in dic: return i
# leetcode submit region end(Prohibit modification and deletion)
