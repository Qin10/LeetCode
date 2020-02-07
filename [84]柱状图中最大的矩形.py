#给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。 
#
# 
#
# 
#
# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。 
#
# 
#
# 
#
# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。 
#
# 
#
# 示例: 
#
# 输入: [2,1,5,6,2,3]
#输出: 10 
# Related Topics 栈 数组



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        maxArea = 0
        heights.append(-1)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                height_idx = stack.pop()
                pre_idx = stack[-1] if stack else -1
                maxArea = max(maxArea, heights[height_idx] * (i - pre_idx - 1))

            stack.append(i)

        return maxArea
#leetcode submit region end(Prohibit modification and deletion)
