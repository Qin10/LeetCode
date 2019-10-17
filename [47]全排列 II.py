# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例: 
#
# 输入: [1,1,2]
# 输出:
# [
#  [1,1,2],
#  [1,2,1],
#  [2,1,1]
# ]
# Related Topics 回溯算法



# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        size = len(nums)
        if size == 0:
            return []
        elif size == 1:
            return [nums]
        res = []
        for i in range(size):
            if i + 1 < size and nums[i] == nums[i + 1]:
                continue
            for j in Solution.permuteUnique(self, nums[:i] + nums[i + 1:]):
                res.append([nums[i]] + j)
        return res

# leetcode submit region end(Prohibit modification and deletion)
