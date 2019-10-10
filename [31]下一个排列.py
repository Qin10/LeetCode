# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。 
#
# 必须原地修改，只允许使用额外常数空间。 
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 1:
            return
        if nums == sorted(nums, reverse=True):
            nums.sort()
            return
        for i in range(-1, -len(nums) - 1, -1):
            if nums[i] >= max(nums[i:]):
                continue
            temp_rest = sorted(nums[i + 1:], reverse=True)
            index = -1
            for k in range(len(temp_rest)):
                if nums[i] < temp_rest[-1]:
                    index = -1
                    break
                elif nums[i] >= temp_rest[k]:
                    index = k - 1
                    break
            temp = nums[i]
            nums[nums.index(temp_rest[index], i)] = temp
            nums[i] = temp_rest[index]
            temp_list = sorted(nums[i + 1:])
            for j in range(-1, -len(temp_list) - 1, -1):
                nums[j] = temp_list[j]
            return
        # leetcode submit region end(Prohibit modification and deletion)
