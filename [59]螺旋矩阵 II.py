# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例: 
#
# 输入: 3
# 输出:
# [
# [ 1, 2, 3 ],
# [ 8, 9, 4 ],
# [ 7, 6, 5 ]
# ]
# Related Topics 数组



# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(n)] for i in range(n)]
        min_row, min_col = 0, 0
        row, col = n, n
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, num, count = 0, 0, 1, 0
        while min_row < row and min_col < col:
            direc = count % 4
            if min_col <= y < col and min_row <= x < row:
                res[x][y] = num
                x += direction[direc][0]
                y += direction[direc][1]
                num += 1
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
