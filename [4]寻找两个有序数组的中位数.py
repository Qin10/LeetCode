# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 
#
# 你可以假设 nums1 和 nums2 不会同时为空。 
#
# 示例 1: 
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
# 
#
# 示例 2: 
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
# 
# Related Topics 数组 二分查找 分治算法



# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        index1 = 0
        index2 = 0
        if nums1 == []:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2) // 2 - 1] + nums2[len(nums2) // 2]) / 2.0
            return nums2[(len(nums2) - 1) // 2] / 1.0
        if nums2 == []:
            if len(nums1) % 2 == 0:
                return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2.0
            return nums1[(len(nums1) - 1) // 2] / 1.0
        while index1 != len(nums1) and index2 != len(nums2):
            if nums1[index1] <= nums2[index2]:
                nums3.append(nums1[index1])
                index1 = index1 + 1
            else:
                nums3.append(nums2[index2])
                index2 = index2 + 1
        if len(nums1) == index1:
            nums3 += nums2[index2:]
        else:
            nums3 += nums1[index1:]
        if len(nums3) % 2 == 0:
            return (nums3[len(nums3) // 2 - 1] + nums3[len(nums3) // 2]) / 2.0
        return nums3[(len(nums3) - 1) // 2] / 1.0

# leetcode submit region end(Prohibit modification and deletion)
