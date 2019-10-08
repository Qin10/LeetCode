# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
# -4 -1 1 2 3 4 5      3  abs(sum-target) = abs(k(固定) + i + j - target)
# Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_diff = abs(nums[0] + nums[1] + nums[2] - target)
        length = len(nums)
        result = nums[0] + nums[1] + nums[2]
        for k in range(length - 2):
            head, last = k + 1, length - 1
            while last > head:
                sum_num = nums[k] + nums[head] + nums[last]
                if sum_num == target:
                    return target
                elif sum_num > target:
                    if sum_num - target >= min_diff:
                        last -= 1
                    elif sum_num - target < min_diff:
                        min_diff = sum_num - target
                        result = sum_num
                else:
                    if target - sum_num >= min_diff:
                        head += 1
                    elif sum_num - target < min_diff:
                        min_diff = target - sum_num
                        result = sum_num
            k += 1
        return result
# leetcode submit region end(Prohibit modification and deletion)
