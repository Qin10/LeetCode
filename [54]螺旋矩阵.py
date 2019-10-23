# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1: 
#
# 输入:
# [
# [ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 
#
# 示例 2: 
#
# 输入:
# [
#  [1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        if row == 0:
            return []
        col = len(matrix[0])
        min_row = 0
        min_col = 0
        res = []
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0
        x = 0
        y = 0
        while min_row <= row and min_col <= col:
            direc = count % 4
            if min_col <= y < col and min_row <= x < row:
                res.append(matrix[x][y])
                x += direction[direc][0]
                y += direction[direc][1]
            elif y == col:
                min_row += 1
                y = col - 1
                x += 1
                count += 1
            elif y < min_col:
                row -= 1
                y = min_col
                x -= 1
                count += 1
            elif x == row:
                col -= 1
                x = row - 1
                y -= 1
                count += 1
            elif x < min_row:
                min_col += 1
                x = min_row
                y += 1
                count += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
