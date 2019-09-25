class Solution:
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
