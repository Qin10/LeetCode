# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。 
#
# 示例: 
#
# 输入:
# [
#   [1,3,1],
#  [1,5,1],
#  [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        p = [[0] * n] * m
        p[0][0] = grid[0][0]
        for i in range(0, m):
            if i != 0:
                p[i][0] = p[i - 1][0] + grid[i][0]
                for j in range(1, n):
                    p[i][j] = min(p[i - 1][j], p[i][j - 1]) + grid[i][j]
            else:
                for j in range(1, n):
                    p[i][j] = p[i][j - 1] + grid[i][j]
        return p[m - 1][n - 1]
# leetcode submit region end(Prohibit modification and deletion)
