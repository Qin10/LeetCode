# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
# 
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。 
#
# 示例: 
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# Related Topics 栈 数组 双指针



# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 自己写的 （栈应该拿来存索引 而不是数值）
        size = len(height)
        if size < 3:
            return 0
        stack = [height[0]]
        res = 0
        for i in range(1, size):
            if height[i] < stack[-1]:
                stack.append(height[i])
            elif height[i] < stack[0]:
                for j in range(1, len(stack)):
                    if stack[j] < height[i]:
                        res += (height[i] - stack[j])
                        stack[j] = height[i]
                stack.append(height[i])
            else:
                for j in stack:
                    res += (stack[0] - j)
                stack = [height[i]]
        return res

    # 动态规划
    # def trap(self, height: List[int]) -> int:
    #     if not height: return 0
    #     n = len(height)
    #     max_left = [0] * n
    #     max_right = [0] * n
    #     max_left[0] = height[0]
    #     max_right[-1] = height[-1]
    #     # 找位置i左边最大值
    #     for i in range(1, n):
    #         max_left[i] = max(height[i], max_left[i - 1])
    #     # 找位置i右边最大值
    #     for i in range(n - 2, -1, -1):
    #         max_right[i] = max(height[i], max_right[i + 1])
    #     # print(max_left)
    #     # print(max_right)
    #     # 求结果
    #     res = 0
    #     for i in range(n):
    #         res += min(max_left[i], max_right[i]) - height[i]
    #     return res

    # 双指针
    # def trap(self, height: List[int]) -> int:
    #     if not height: return 0
    #     left = 0
    #     right = len(height) - 1
    #     res = 0
    #     # 记录左右边最大值
    #     left_max = height[left]
    #     right_max = height[right]
    #     while left < right:
    #         if height[left] < height[right]:
    #             if left_max > height[left]:
    #                 res += left_max - height[left]
    #             else:
    #                 left_max = height[left]
    #             left += 1
    #         else:
    #             if right_max > height[right]:
    #                 res += right_max - height[right]
    #             else:
    #                 right_max = height[right]
    #             right -= 1
    #     return res

    # 栈
    # def trap(self, height: List[int]) -> int:
    #     if not height: return 0
    #     n = len(height)
    #     stack = []
    #     res = 0
    #     for i in range(n):
    #         # print(stack)
    #         while stack and height[stack[-1]] < height[i]:
    #             tmp = stack.pop()
    #             if not stack: break
    #             res += (min(height[i], height[stack[-1]]) - height[tmp]) * (i - stack[-1] - 1)
    #         stack.append(i)
    #     return res


# leetcode submit region end(Prohibit modification and deletion)
