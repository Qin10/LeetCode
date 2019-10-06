# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。 
#
# 示例: 
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 
# Related Topics 数组 哈希表



# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # O(n*n)
    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        """暴力法"""
        # 遍历数组中的元素
        for i in range(len(nums)):
            # 如果与target的差在数组中且不为本身，则输出
            if target - nums[i] in nums:
                if nums.index(target - nums[i]) != i:
                    return [i, nums.index(target - nums[i])]
        return None

    # O(n)
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        """用字典存储数组，字典查找速度快于数组"""
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None

# leetcode submit region end(Prohibit modification and deletion)
